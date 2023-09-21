# coding=utf-8
import pickle
import random
import time

import pycore.data.entity.globalvar as gl
from pycore.data.entity import config
from pycore.utils import time_utils

from game_base.base.constant import REDIS_ROOM_MAP, REDIS_ACCOUNT_GAME, REDIS_UNION_ROOM_MAP, REDIS_ROOM_TIMEOUT_LIST, \
    REDIS_PLAYER_WIN, REDIS_UNION_ROOM_ROBOT_COUNT
from game_base.base.game.mode.game_status import GameStatus
from game_base.base.game.mode.timeout_type import TimeoutType
from game_base.base.protocol.base.base_pb2 import ENTER_ROOM, UPDATE_GAME_INFO, UPDATE_GAME_PLAYER_INFO, SELF_INFO, \
    REENTER_GAME_INFO, START_GAME, EXECUTE_ACTION, UNKNOWN_ERROR, STAND_UP, DISSOLVE, DISSOLVE_CONFIRM
from game_base.base.protocol.base.game_base_pb2 import RecGpsInfo, RecUpdateGameInfo, RecUpdateGameUsers, \
    RecReEnterGameInfo, RecExecuteAction, RecDissolved, RecDissolvedConfirm
from game_base.base.send_message import send_to_gateway
from game_base.mode.data import club_member, base_mode
from game_base.mode.data.big_data_control import BigDataControl
from game_base.mode.data.line_control import LineControl
from game_base.mode.data.player_control import PlayerControl
from game_base.utils import int_utils


def seat2_user_info(seat, user_info):
    u"""
    座位转用户信息
    :param seat: 座位
    :param user_info: 用户信息
    :return: 用户信息
    """
    user_info.playerId = seat.user_id
    user_info.account = seat.account
    user_info.nick = seat.nickname
    user_info.headUrl = seat.head
    user_info.sex = seat.sex
    user_info.ip = seat.ip
    user_info.address = seat.address
    if None is not seat.gps_info:
        user_info.gpsInfo = seat.gps_info
    user_info.ready = seat.ready
    user_info.score = seat.score - seat.play_score
    # user_info.playScore = seat.play_score
    # user_info.banker = self.banker == seat.seat_no
    user_info.seatNo = seat.seat_no
    user_info.createTime = seat.create_time
    user_info.online = seat.online
    if 0 != seat.leave_seat:
        leave_time = seat.leave_seat - int(time.time())
        if leave_time > 0:
            user_info.leaveSeat = leave_time
    return user_info


def get_room(room_key):
    u"""
    通过房间号获取房间
    :param room_key:
    :return:
    """
    room_no_info = room_key.split(',')
    if room_no_info[1] == '0':
        return gl.get_v("redis").hgetobj(REDIS_ROOM_MAP, room_no_info[0])
    else:
        return gl.get_v("redis").hgetobj(REDIS_UNION_ROOM_MAP + room_no_info[1], room_no_info[0])


def exist_room(room_no):
    u"""
    房间是否存在
    :param room_no:
    :return:
    """
    room_no_info = room_no.split(',')
    if room_no_info[1] == '0':
        return gl.get_v("redis").hexists(REDIS_ROOM_MAP, room_no_info[0])
    else:
        return gl.get_v("redis").hexists(REDIS_UNION_ROOM_MAP + room_no_info[1], room_no_info[0])


class Room(object):

    def __init__(self) -> None:
        self.room_no = None
        self.game_id = 0
        self.game_type = 0  # 0.房卡 1.金币 2.比赛分
        self.pay_type = 0
        self.score = 0
        self.in_score = 0
        self.leave_score = 0
        self.game_times = 0
        self.times_type = 0
        self.people_count = 0
        self.people_start = 0
        self.leave_type = 0
        self.game_rules = 0
        self.gps_limit = 0
        self.match_level = 0
        self.watch_seats = []
        self.seats = []
        self.seat_nos = []
        self.start_time = int(time.time())
        self.game_status = GameStatus.WAITING
        self.history_actions = []
        self.room_owner = 0
        self.current_game_times = 0
        self.operation_time = 0
        self.last_operation_time = 0
        self.desk_score = 0
        self.banker = 0
        self.min_score = 0
        self.operation_seat = 0
        self.dissolved_timeout = None
        self.dissolved_time = 0
        self.record_ids = []
        self.total_win_lose = {}
        self.union_id = 0
        self.room_config_id = 0
        self.control_seat = None
        self.lose_seat = None

        # 下面是联盟里面抽水分成数据
        self.union_cost = 0
        self.allocation_type = 0
        self.charge_target = 0
        self.charge_type = 0
        self.charge_rate = 0
        self.charge_value = 0
        self.cost = 0
        self.cost_rate = 0
        self.hierarchies = []

        self.robot_count = 0

    def save(self):
        u"""
        保存房间信息
        """
        if 0 == self.union_id:
            if self.game_status != GameStatus.DESTORY:
                gl.get_v("redis").hsetobj(REDIS_ROOM_MAP, self.room_no, self)
            else:
                gl.get_v("redis").hdelobj(REDIS_ROOM_MAP, self.room_no)
                # gl.get_v("redis").hdelobj(REDIS_UNION_ROOM_ROBOT_COUNT + str(self.union_id), self.room_no)
                del self
        else:
            if self.game_status != GameStatus.DESTORY:
                gl.get_v("redis").hsetobj(REDIS_UNION_ROOM_MAP + str(self.union_id), self.room_no, self)
            else:
                gl.get_v("redis").hdelobj(REDIS_UNION_ROOM_MAP + str(self.union_id), self.room_no)
                gl.get_v("redis").hdelobj(REDIS_UNION_ROOM_ROBOT_COUNT + str(self.union_id), self.room_no)
                del self

    def get_room_key(self):
        return '%s,%s' % (self.room_no, str(self.union_id))

    def get_cache_win_name(self):
        return REDIS_PLAYER_WIN + str(self.game_type) + '_' + str(self.game_id) + '_' + str(self.score) + '_' + str(
            time_utils.get_today_earliest_by_timezone(-14400))

    def clear(self):
        self.game_status = GameStatus.WAITING
        self.desk_score = 0
        self.min_score = 0
        self.operation_seat = 0
        self.history_actions.clear()
        self.control_seat = None
        self.lose_seat = None
        for s in self.seats:
            s.clear()
        for s in self.watch_seats:
            s.clear()

    def room_over(self):
        pass

    def get_game_rule(self, index):
        int_utils.has_bit(self.game_rules, index)

    def get_seat_by_seat_no(self, seat_no):
        for s in self.seats:
            if s.seat_no == seat_no:
                return s
        return None

    def get_seat_by_account(self, user_id):
        for s in self.seats:
            if s.user_id == user_id:
                return s
        return None

    def get_watch_seat_by_account(self, user_id):
        for s in self.watch_seats:
            if s.user_id == user_id:
                return s
        return None

    def get_playing_count(self):
        count = 0
        for s in self.seats:
            if s.gaming and not s.end:
                count += 1
        return count

    def get_gpa_info(self):
        rec_gps_info = RecGpsInfo()
        for seat in self.seats:
            gps_player_info = rec_gps_info.playerInfos.add()
            gps_player_info.gpsInfo = seat.gps_info
            gps_player_info.playerId = seat.user_id
        return rec_gps_info

    def join_room(self, account, ip):
        send_to_gateway(ENTER_ROOM, None, account.id)
        send_to_gateway(UPDATE_GAME_INFO, self.update_game_info().SerializeToString(), account.id)
        seat = self.get_seat_by_account(account.id)
        if seat is None:
            seat = self.get_watch_seat_by_account(account.id)
        user_info = seat2_user_info(seat, RecUpdateGameUsers.UserInfo())
        send_to_gateway(SELF_INFO, user_info.SerializeToString(), account.id)
        self.update_player_info(account.id)
        if self.game_status != GameStatus.WAITING:
            self.reenter_game_info(account.id)
        gl.get_v("redis").hset(REDIS_ACCOUNT_GAME, account.id,
                               '%s,%s,%d' % (self.room_no, self.union_id, self.game_type))
        self.save()

    def stand_up(self, user_id):
        seat = self.get_seat_by_account(user_id)
        if None is not seat:
            self.seat_nos.append(seat.seat_no)
            seat.seat_no = 0
            self.watch_seats.append(seat)
            self.seats.remove(seat)
            send_to_gateway(STAND_UP, None, user_id)
            self.update_player_info(0)
            return
        send_to_gateway(STAND_UP, None, user_id, UNKNOWN_ERROR)
        self.check_ready()

    def reconnect(self, user_id, ip):
        seat = self.get_seat_by_account(user_id)
        if None is seat:
            seat = self.get_watch_seat_by_account(user_id)
        if seat is not None:
            seat.ip = ip
            seat.online = True
            send_to_gateway(ENTER_ROOM, None, user_id)
            send_to_gateway(UPDATE_GAME_INFO, self.update_game_info().SerializeToString(), user_id)
            user_info = seat2_user_info(seat, RecUpdateGameUsers.UserInfo())
            send_to_gateway(SELF_INFO, user_info.SerializeToString(), user_id)
            self.update_player_info(0)
            if self.game_status != GameStatus.WAITING:
                self.reenter_game_info(user_id)

    def update_game_info(self):
        update_game_info = RecUpdateGameInfo()
        update_game_info.roomNo = self.room_no
        update_game_info.gameState = self.game_status
        update_game_info.curPlayCount = self.current_game_times
        update_game_info.unionId = self.union_id
        update_game_info.createRoom.gameId = self.game_id
        update_game_info.createRoom.gameType = self.game_type
        update_game_info.createRoom.payType = self.pay_type
        update_game_info.createRoom.baseScore = self.score
        update_game_info.createRoom.inScore = self.in_score
        update_game_info.createRoom.leaveScore = self.leave_score
        update_game_info.createRoom.gameTimes = self.game_times
        update_game_info.createRoom.timesType = self.times_type
        update_game_info.createRoom.peopleCount = self.people_count
        update_game_info.createRoom.peopleStart = self.people_start
        update_game_info.createRoom.leaveType = self.leave_type
        update_game_info.createRoom.gameRules = self.game_rules
        update_game_info.createRoom.gpsLimit = self.gps_limit
        update_game_info.createRoom.operationTime = self.operation_time
        return update_game_info

    def update_player_info(self, user_id):
        game_users = self.player_info()
        if 0 == user_id:
            self.broadcast_all_to_gateway(UPDATE_GAME_PLAYER_INFO, game_users.SerializeToString())
        else:
            send_to_gateway(UPDATE_GAME_PLAYER_INFO, game_users.SerializeToString(), user_id)

    def player_info(self):
        game_users = RecUpdateGameUsers()
        for seat in self.seats:
            seat2_user_info(seat, game_users.users.add())
        return game_users

    def reenter_game_info(self, user_id):
        game_info = RecReEnterGameInfo()
        for a in self.history_actions:
            execute_action = game_info.actionInfos.add()
            execute_action.ParseFromString(a)
        send_to_gateway(REENTER_GAME_INFO, game_info.SerializeToString(), user_id)

    def check_ready(self):
        if self.game_status == GameStatus.WAITING:
            all_ready = True
            for seat in self.seats:
                if (not seat.ready or seat.score < self.in_score) and 0 == seat.leave_seat:
                    all_ready = False
                    break
            if all_ready:
                self.start()

    def update_dissolved(self):
        rec_dissolved = RecDissolved()
        if 0 != self.dissolved_time:
            rec_dissolved.time = self.dissolved_time - int(time.time())
        for seat in self.seats:
            if self.game_status == GameStatus.WAITING or seat.gaming:
                dissolved = rec_dissolved.dissolved.add()
                dissolved.playerId = seat.user_id
                if None is not seat.dissolved:
                    dissolved.status = 1 if seat.dissolved else 2
        self.broadcast_seat_to_gateway(DISSOLVE, rec_dissolved.SerializeToString())

    def check_dissolved(self):
        all_count = 0
        agree_count = 0
        rejected_count = 0
        for seat in self.seats:
            if self.game_status == GameStatus.WAITING or seat.gaming:
                all_count += 1
                if None is seat.dissolved:
                    continue
                if seat.dissolved:
                    agree_count += 1
                else:
                    rejected_count += 1
        rec_dissolved = RecDissolvedConfirm()
        if rejected_count > 0:
            gl.get_v("redis").zrem(REDIS_ROOM_TIMEOUT_LIST + str(self.game_id), self.dissolved_timeout)
            self.dissolved_timeout = None
            rec_dissolved.dissolved = False
            self.broadcast_seat_to_gateway(DISSOLVE_CONFIRM, rec_dissolved.SerializeToString())
            return
        if all_count == agree_count:
            gl.get_v("redis").zrem(REDIS_ROOM_TIMEOUT_LIST + str(self.game_id), self.dissolved_timeout)
            self.dissolved_timeout = None
            rec_dissolved.dissolved = True
            self.broadcast_seat_to_gateway(DISSOLVE_CONFIRM, rec_dissolved.SerializeToString())
            self.room_over()

    def clear_dissolved(self):
        for seat in self.seats:
            seat.dissolved = None

    def start(self):
        if self.game_status == GameStatus.WAITING:
            if len(self.seats) - self.leave_seat_people() < self.get_start_people():
                gl.get_v("serverlogger").logger.exception("user count < start_people, cant start")
                return
            self.broadcast_seat_to_gateway(START_GAME, None)
            # 单控
            control_seats = set()
            # 大数据控
            cache_win_name = self.get_cache_win_name()
            controls = base_mode.query(PlayerControl, 0, union_id=self.union_id, game_id=self.game_id,
                                       game_type=self.game_type, score=self.score, is_finish=0)
            line_controls = base_mode.query(LineControl, 0, union_id=self.union_id, game_id=self.game_id,
                                            game_type=self.game_type, score=self.score, is_finish=0)
            agent_users = {}
            for line_control in line_controls:
                if line_control.id in agent_users:
                    continue
                users = set()
                users.add(line_control.id)
                user_ids = club_member.userids_by_agent(line_control.club_id, line_control.id)
                users = users.union(user_ids)
                agent_users[str(line_control.id)] = users
            big_data_controls = base_mode.query(BigDataControl, 0, game_id=self.game_id, game_type=self.game_type, )

            line_control_seats = []
            line_control_win = None
            big_data_seat = None
            big_data_seat_score = None
            for seat in self.seats:
                if 0 == seat.leave_seat:
                    seat.score += seat.take_score
                    seat.take_score = 0
                    seat.ready = False
                    seat.gaming = True
                    total = 0
                    if gl.get_v("redis").hexists(cache_win_name, seat.user_id):
                        total = float(gl.get_v("redis").hget(cache_win_name, seat.user_id))
                    # 单控
                    for control in controls:
                        if control.id == seat.account:
                            if 0 == control.min_value and 0 == control.max_value and 0 != control.finish_value:
                                if control.finish_value > control.current_value:
                                    if control.rate > random.randint(0, 99):
                                        control_seats.add(seat)
                                else:
                                    base_mode.update(PlayerControl, {'is_finish': True})
                            else:
                                if control.min_value > control.current_value:
                                    if control.rate > random.randint(0, 99):
                                        control_seats.add(seat)
                                elif control.max_value < control.current_value:
                                    if control.rate > random.randint(0, 99):
                                        self.lose_seat = seat
                    # 线控
                    for control in line_controls:
                        if control.id in agent_users and seat.user_id in agent_users[str(control.id)]:
                            line_control_seats.append(seat)
                            if 0 == control.min_value and 0 == control.max_value and 0 != control.finish_value:
                                if control.finish_value > control.current_value:
                                    if control.rate > random.randint(0, 99):
                                        line_control_win = True
                                else:
                                    base_mode.update(LineControl, {'is_finish': True})
                            else:
                                if control.min_value > control.current_value:
                                    if control.rate > random.randint(0, 99):
                                        line_control_win = True
                                elif control.max_value < control.current_value:
                                    if control.rate > random.randint(0, 99):
                                        line_control_win = False

                    if (None is big_data_seat_score or total < big_data_seat_score) and seat != self.lose_seat:
                        big_data_seat_score = total
                        big_data_seat = seat
            # 没有单控执行线控
            if 0 == len(control_seats):
                if None is not line_control_win:
                    if line_control_win:
                        self.control_seat = random.choice(list(line_control_seats))
                    elif None is self.lose_seat:
                        self.lose_seat = random.choice(list(line_control_seats))
            # 没有单控才执行群控
            if 0 == len(control_seats):
                for big_data_control in big_data_controls:
                    if -big_data_seat_score > self.score * float(big_data_control.score) and (
                            big_data_control.rate > random.randint(0, 99)):
                        control_seats.add(big_data_seat)
            if 0 != len(control_seats):
                self.control_seat = random.choice(list(control_seats))
            else:
                self.control_seat = big_data_seat

    def change_operation(self):
        thisop = self.operation_seat
        next_seat_no = self.get_next_seat(self.operation_seat)
        next_operation = self.get_seat_by_seat_no(next_seat_no)
        count = 0
        while None is next_operation or next_operation.end or not next_operation.gaming or 0 == next_operation.score - next_operation.play_score - next_operation.play_mangguo:
            next_seat_no = self.get_next_seat(next_seat_no)
            next_operation = self.get_seat_by_seat_no(next_seat_no)
            count += 1
            if thisop == next_seat_no or count == self.people_count:
                return 0
        self.operation_seat = next_seat_no
        return self.operation_seat

    def get_next_seat(self, next_seat):
        next_seat += 1
        if next_seat > self.people_count:
            return 1
        return next_seat

    def execute_action(self, user_id, action_type, data):
        execute_action = RecExecuteAction()
        execute_action.actionType = action_type
        execute_action.playerId = user_id
        if data is not None:
            execute_action.data = data
        self.broadcast_all_to_gateway(EXECUTE_ACTION, execute_action.SerializeToString())
        self.history_actions.append(execute_action.SerializeToString())

    def leave_seat_people(self):
        leave_count = 0
        for seat in self.seats:
            if 0 != seat.leave_seat:
                leave_count += 1
        return leave_count

    def get_start_people(self):
        if self.current_game_times == 0:
            return self.people_start
        return 2

    def broadcast_seat_to_gateway(self, opcode, data, skip=None):
        if skip is None:
            skip = []
        for seat in self.seats:
            if seat.user_id not in skip:
                send_to_gateway(opcode, data, seat.user_id)

    def broadcast_watch_to_gateway(self, opcode, data, skip=None):
        if skip is None:
            skip = []
        for seat in self.watch_seats:
            if seat.user_id not in skip:
                send_to_gateway(opcode, data, seat.user_id)

    def broadcast_all_to_gateway(self, opcode, data, skip=None):
        self.broadcast_seat_to_gateway(opcode, data, skip)
        self.broadcast_watch_to_gateway(opcode, data, skip)

    def add_dissolved_timeout(self):
        dissolved_time = int(config.get("game", "dissolved_time"))
        if 0 != dissolved_time:
            if None is not self.dissolved_timeout:
                gl.get_v("redis").zrem(REDIS_ROOM_TIMEOUT_LIST + str(self.game_id),
                                       self.dissolved_timeout)
                self.dissolved_timeout = None
            data = pickle.dumps({"timeout_type": TimeoutType.DISSOLVED, "room_no": self.get_room_key()}, -1)
            self.dissolved_timeout = data
            op_time = int(time.time()) + dissolved_time
            self.dissolved_time = op_time
            gl.get_v("redis").zadd(REDIS_ROOM_TIMEOUT_LIST + str(self.game_id), {data: op_time})
