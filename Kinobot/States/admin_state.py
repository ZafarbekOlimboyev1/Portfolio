from aiogram.fsm.state import State,StatesGroup

class AdminState(StatesGroup):
    upload_movie = State()
    title = State()
    about = State()
    key = State()
    send_msg = State()
    new_admin = State()
    del_admin = State()
    sub_id = State()
    c_channel = State()
    id_channel = State()
    verfy_channel_info = State()
    del_channel = State()
    delete_admin = State()
    name = State()
    name_for_list = State()
