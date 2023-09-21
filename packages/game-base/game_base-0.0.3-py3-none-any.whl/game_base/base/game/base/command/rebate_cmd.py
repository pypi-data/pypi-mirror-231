# coding=utf-8
import math

from pycore.data.entity import globalvar as gl
from sqlalchemy.orm import load_only

from game_base.base.constant import REDIS_ACCOUNT_CLUB
from game_base.base.mode import game_type, currency_type
from game_base.mode.data import base_mode, club_history, currency
from game_base.mode.data.club_member import ClubMember
from game_base.mode.data.union import Union
from game_base.mode.data.union_member import UnionMember


def execute(room, total_win_lose_items):
    r"""
    抽水分成
    :param room: 房间信息
    :param total_win_lose_items: 输赢信息
    :return:
    """
    if game_type.GOLD == room.game_type or game_type.UNION_GOLD == room.game_type:
        _currency_type = currency_type.GOLD
        _currency_union = 0
    elif game_type.UNION_SCORE == room.game_type:
        _currency_type = currency_type.UNION_SCORE
        _currency_union = room.union_id
    else:
        return
    union = None
    if 0 != room.union_id:
        union = base_mode.get(Union, room.union_id)
    if None is union:
        return
    # 抽水
    total_charge = 0
    charge = {}
    cost = 0
    # 所有赢家
    if 0 == room.charge_type:
        charge_count = 0
        for k, v in total_win_lose_items:
            if v['score'] > 0:
                charge[k] = math.floor(v['score'] * room.charge_rate * 100) / 100
                currency.operation_currency(k, _currency_type, -charge[k], 0, currency_type.GAME_FEES,
                                            '%s,%d' % (room.room_no, room.game_id), _currency_union)
                total_charge += charge[k]
                if 0 != room.cost_rate:
                    cost += math.floor(charge[k] * room.cost_rate * 100) / 100
                charge_count += 1
                if charge_count == room.charge_target:
                    break
            else:
                break
        if 0 != room.cost:
            cost += room.cost
    # 每人消耗
    elif 1 == room.charge_type:
        for k, v in total_win_lose_items:
            charge[k] = room.charge_type
            currency.operation_currency(k, _currency_type, -charge[k], 0, currency_type.GAME_FEES,
                                        '%s,%d' % (room.room_no, room.game_id), _currency_union)
            total_charge += charge[k]
        cost += room.cost
    # 阶梯
    elif 2 == room.charge_type:
        charge_count = 0
        for k, v in total_win_lose_items:
            if v['score'] > 0:
                charge_item = 0
                cost_item = 0
                hierarchies_items = sorted(room.hierarchies.items(), key=lambda d: d['win'], reverse=True)
                for hierarchy in hierarchies_items:
                    if hierarchy.win < v['score'] and charge_item < hierarchy.charge_value:
                        charge_item = hierarchy.charge_value
                        cost_item = hierarchy.cost
                    else:
                        break
                if 0 != charge_item:
                    charge[k] = charge_item
                    currency.operation_currency(k, _currency_type, -charge[k], 0, currency_type.GAME_FEES,
                                                '%s,%d' % (room.room_no, room.game_id), _currency_union)
                    total_charge += charge[k]
                    cost += cost_item
                    charge_count += 1
                    if charge_count == room.charge_target:
                        break
            else:
                break

    # 分成
    if total_charge < cost:
        cost = total_charge
    score_charge = total_charge - cost
    score_rel_charge = 0
    # 分成比例计算
    user_rebate = {}
    if 0 < score_charge:
        # 赢家分
        if 0 == room.allocation_type:
            # 比赛分成
            for k, v in charge.items():
                user_rebate[k] = math.floor(score_charge * (v / total_charge) * 100) / 100
        elif 1 == room.allocation_type:
            total_flow = 0
            for k, v in total_win_lose_items:
                total_flow += abs(v['score'])
            for k, v in total_win_lose_items:
                user_rebate[k] = math.floor(score_charge * (abs(v['score']) / total_flow) * 100) / 100
        elif 2 == room.allocation_type:
            for k, v in total_win_lose_items:
                user_rebate[k] = math.floor(score_charge / len(total_win_lose_items) * 100) / 100
        # 比赛分成
        score_rebate = {}
        for k, v in user_rebate.items():
            if gl.get_v("redis").hexists(REDIS_ACCOUNT_CLUB, k):
                club_id = gl.get_v("redis").hget(REDIS_ACCOUNT_CLUB, k)
                if not base_mode.query(UnionMember, -1, club_id=club_id, union_id=club_id):
                    club_id = club_history.last_club_id(k)
                agent = base_mode.query_values(ClubMember, load_only(ClubMember.agent_ids, ClubMember.agent), 1,
                                               club_id=club_id, user_id=k)
                if None is not agent.agent_ids:
                    total_score = v
                    score_rel_charge += total_score
                    up_agent_id = None
                    agents = agent.agent_ids.split(',')
                    if agent.agent:
                        agents.append(k)
                    for agent_id in agents:
                        member = base_mode.query(ClubMember, 1, club_id=club_id, user_id=agent_id)
                        if None is member:
                            continue
                        if agent_id not in score_rebate:
                            score_rebate[agent_id] = 0
                        rebate = math.floor(total_score * float(member.score_ratio) * 100) / 100
                        score_rebate[agent_id] += rebate
                        if None is not up_agent_id:
                            score_rebate[up_agent_id] -= rebate
                        up_agent_id = agent_id

        for k, v in score_rebate.items():
            currency.operation_currency(k, _currency_type, 0, v, currency_type.SCORE_REBATE,
                                        '%s,%d' % (room.room_no, room.game_id), _currency_union)
        # 剩余的给圈主
        if score_rel_charge < score_charge:
            currency.operation_currency(union.owner_id, _currency_type, 0, score_charge - score_rel_charge,
                                        currency_type.SCORE_REBATE, '%s,%d' % (room.room_no, room.game_id),
                                        _currency_union)
        print('抽水')
        print(charge)
        print('保底')
        print(cost)
        print('用于分成的')
        print(score_charge)
        print('实际分成的')
        print(score_rel_charge)
        print('实际分成')
        print(user_rebate)
        print('实际分成分数')
        print(score_rebate)
    if 0 == cost:
        return
    if cost > room.union_cost:
        cost -= room.union_cost
        currency.operation_currency(union.owner_id, _currency_type, 0, room.union_cost, currency_type.GUARANTEES,
                                    '%s,%d' % (room.room_no, room.game_id), _currency_union)
    elif cost < room.union_cost:
        currency.operation_currency(union.owner_id, _currency_type, 0, cost, currency_type.GUARANTEES,
                                    '%s,%d' % (room.room_no, room.game_id), _currency_union)
        return
    if 0 < cost:
        # 保底分成
        rel_cost = 0
        # 保底分成比例
        user_cost = {}
        for k, v in total_win_lose_items:
            user_cost[k] = math.floor(cost / len(total_win_lose_items) * 100) / 100
        # 保底分成
        cost_rebate = {}
        for k, v in user_cost.items():
            if gl.get_v("redis").hexists(REDIS_ACCOUNT_CLUB, k):
                club_id = gl.get_v("redis").hget(REDIS_ACCOUNT_CLUB, k)
                if not base_mode.query(UnionMember, -1, club_id=club_id, union_id=club_id):
                    club_id = club_history.last_club_id(k)
                agent = base_mode.query_values(ClubMember, load_only(ClubMember.agent_ids, ClubMember.agent), 1,
                                               club_id=club_id, user_id=k)
                if None is not agent.agent_ids:
                    total_score = v
                    rel_cost += total_score
                    up_agent_id = None
                    agents = agent.agent_ids.split(',')
                    if agent.agent:
                        agents.append(k)
                    for agent_id in agents:
                        member = base_mode.query(ClubMember, 1, club_id=club_id, user_id=agent_id)
                        if None is member:
                            continue
                        if not agent_id in cost_rebate:
                            cost_rebate[agent_id] = 0
                        rebate = math.floor(total_score * float(member.guarantees_ratio) * 100) / 100
                        cost_rebate[agent_id] += rebate
                        if None is not up_agent_id:
                            cost_rebate[up_agent_id] -= rebate
                        up_agent_id = agent_id
        for k, v in cost_rebate.items():
            currency.operation_currency(k, _currency_type, 0, v, currency_type.GUARANTEES_REBATE,
                                        '%s,%d' % (room.room_no, room.game_id), _currency_union)
        # 剩余的给圈主
        if rel_cost < cost:
            currency.operation_currency(union.owner_id, _currency_type, 0, cost - rel_cost,
                                        currency_type.GUARANTEES_REBATE, '%s,%d' % (room.room_no, room.game_id),
                                        _currency_union)
        print('保底分成')
        print(user_cost)
        print('保底分成分数')
        print(cost_rebate)
        print('实际保底分成的')
        print(rel_cost)
