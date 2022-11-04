from random import randrange

temp_list = ["Bem vindo <@{}>, seu fodido!",
             "Seja Bem Vindo <@{}>. Agora vai pro caralho!"]


def get_welcome_message(new_member_id) -> str:
    return __get_template().format(new_member_id)


def __get_template() -> str:
    msg_pos = randrange(len(temp_list))

    print(f'Message "{temp_list[msg_pos]}" selected')

    return temp_list[msg_pos]
