```shell
$ mediathequeroubaix config create

Config: /home/johndoe/.config/mediathequeroubaix/config.json

╭──────────────────────────────────────────────────────────────────────────────╮
│ Config(                                                                      │
│     users=[                                                                  │
│         User(                                                                │
│             login='X001002003',                                              │
│             password='password00'                                            │
│         )                                                                    │
│     ]                                                                        │
│ )                                                                            │
╰──────────────────────────────────────────────────────────────────────────────╯
```

```shell
$ mediathequeroubaix config show

Config: /home/johndoe/.config/mediathequeroubaix/config.json

╭──────────────────────────────────────────────────────────────────────────────╮
│ Config(                                                                      │
│     users=[                                                                  │
│         User(                                                                │
│             login='X001002003',                                              │
│             password='password00'                                            │
│         )                                                                    │
│     ]                                                                        │
│ )                                                                            │
╰──────────────────────────────────────────────────────────────────────────────╯
```

```shell
$ mediathequeroubaix loans list
Getting loans of X001002003
                               John DOE: 2 loans
┏━━━━━━━┯━━━━━━━━━┯━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━┯━━━━━━━━━━━┓
┃   #   │ Barcode │ Call number │ Title                       │  Due date  │ Renewable ┃
┠───────┼─────────┼─────────────┼─────────────────────────────┼────────────┼───────────┨
┃  1/10 │ C123456 │ E BD/ALL    │ FP in Python                │ 27/12/2022 │    ✅     ┃
┃  2/10 │ C234567 │ SF/PRI      │ Machine Learning for Humans │ 03/12/2022 │    ❌     ┃
┗━━━━━━━┷━━━━━━━━━┷━━━━━━━━━━━━━┷━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┷━━━━━━━━━━━━┷━━━━━━━━━━━┛
```

```shell
$ mediathequeroubaix loans renew
Renewing loans of user 'X001002003'
Will renew 1 loans for John Doe
                               John DOE: 2 loans
┏━━━━━━━┯━━━━━━━━━┯━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━┯━━━━━━━━━━━┓
┃   #   │ Barcode │ Call number │ Title                       │  Due date  │ Renewable ┃
┠───────┼─────────┼─────────────┼─────────────────────────────┼────────────┼───────────┨
┃  1/10 │ C123456 │ E BD/ALL    │ FP in Python                │ 17/01/2023 │    ❌     ┃
┃  2/10 │ C234567 │ SF/PRI      │ Machine Learning for Humans │ 03/12/2022 │    ❌     ┃
┗━━━━━━━┷━━━━━━━━━┷━━━━━━━━━━━━━┷━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┷━━━━━━━━━━━━┷━━━━━━━━━━━┛
```
