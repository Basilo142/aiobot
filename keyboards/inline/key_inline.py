from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import buy_callback

inline_buttons = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(
                                                  text='first inline',
                                                  callback_data=buy_callback.new(item='1_first_inline', name='*')
                                              ),
                                              InlineKeyboardButton(
                                                  text='second inline',
                                                  callback_data=buy_callback.new(item='2_inline', name='**')
                                              )

                                          ],
                                          [
                                              InlineKeyboardButton(
                                                  text='CANCEL',
                                                  callback_data='cancel'
                                              )
                                          ]
                                      ])
drugaya_key = InlineKeyboardMarkup()
DRUG = 'https://docs.google.com/spreadsheets/d/1uxD47jYJm5x6pRJw9AQ_I8UC53EO9LYGbXRnbeMNqWE/edit#gid=1590717052'
drug = InlineKeyboardButton(text='asdasdasda', url=DRUG)
drugaya_key.insert(drug)
