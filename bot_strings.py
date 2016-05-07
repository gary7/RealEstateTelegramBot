# -*- coding: utf-8 -*-
import re

# User
# None state
hello_message = "Добро пожаловать в бот аренды. Для продолжения введите инвайт."
auth_failed = "Авторизация провалена. Инвайт неверен. Осталось попыток: "
auth_finished = "Авторизация успешна."
auth_totally_failed = "Авторизация запрещена. Не осталось попыток."
start_id = '/start'

# Main state
main_help = """Добро пожаловать в бот аренды квартир.
Доступны следующие команды:
/help Напечатать это сообщение.
/add_link Добавить ссылку.
/get_links Получить список текущих ссылок.
/set_updates Установить частоту обновлений по ссылкам."""
wrong_command = "Неверная команда. Наберите /help для помощи."
help_id = '/help'
add_link_id = '/add_link'
get_links_id = '/get_links'
set_updates_id = '/set_updates'

# Admin only
invoke_invites = '/invites_invoke'
admin_hello = "Hello, admin!"

current_links_message = "Список текущих ссылок:"
no_links_message = "Ссылок нет."

awaitance_time_exceeded = "Превышено время ожидания. Повторите попытку."
cancel_id = '/cancel'

add_link_enter = "Введите ссылку или /cancel для отмены"
add_link_failed = "Добавление ссылки \"{tag}\" не удалось. Попробуйте ещё раз, набрав /add_link"
add_link_success = "Добавление ссылки \"{tag}\" успешно."

add_link_tag_enter = "Введите метку для ссылки. Например: \"1 комната в центре до 30к\" (максимум 30 символов)."
add_link_tag_wrong_tag = "Метка неверна. Проверьте её длину. Для отмены введите /cancel."
add_link_queue_notification = "Мы проверим ссылку, а вам вскоре вам придет уведомление о результате."
updates_time_not_setted_up = "Частота обновлений задана по умолчанию (60 минут)." \
                             "Вы можете изменить её при помощи команды /set_updates."

set_updates_enter_message = "Введите время (в минутах) о том, как часто" \
                            " бы вы хотели получать уведомления о новых квартирах" \
                            " (минимум 60 минут). /cancel для отмены"
set_updates_wrong_time_str = "Кажется, это не время в минутах (введите число). Попробуйте ещё раз." \
                             " /cancel для отмены"
set_updates_wrong_duration = "Минимумальное время между обновлениями -- это 60 минут. Попробуйте ещё раз." \
                             " /cancel для отмены."
set_updates_success = "Частота обновлений успешна установлена."

base_for_sending_flat = """Адрес:
Метро: {metro}
Адрес: {address}

Информация:
Объект: {object}
Площади: {sizes_total}
Этаж: {floor}

Цена:
{price} ({price_info})
Процент: {percent}

Дополнительные сведения:
{additional_info}

Комментарий:
{comment}

Контакты:
{contacts}
"""
go_to_flat_by_url_caption = "Открыть в браузере"
base_for_sending_preview = "{location} {price} {info_cmd}"
cian_base_cmd = "/cian{id}"
cian_cmd_regexp = re.compile("\/cian([0-9]+)")

no_flat_with_id = "Квартиры с таким id не найдено"
