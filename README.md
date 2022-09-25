# Channel watcher bot

## How to use

Install dependencies using `requirements.txt`

```shell
pip install --user -r requirements.txt
```

Install node.js development dependencies

```shell
yarn install
```

Copy `.env.example` to `.env`

The clients implementation try to use **BOT_SESSION** and **USER_SESSION** variables, if dont exist, it use **API_ID**, **API_HASH**, and **BOT_TOKEN** variables.

I recomend use session string in production. To get the current bot and user session string, first configure in the `.env` the **API_ID**, **API_HASH**, and **BOT_TOKEN** and run the command below, it start both clients and save the session string in the `.env` automatically.

```shell
python session.py
```

Remember only push to production the `.env` file with **API_ID**, **API_HASH**, and **BOT_TOKEN** empty and remove `bot.session` and `user.session`. You can use the command below

```shell
python clean.py
```

Start the bot

```shell
python main.py
```

In dev mode, I recommend use nodemon to restart the command automatically

Start bot

```shell
yarn nodemon main.py
```

## Environment variables

> Get the **API_ID** and **API_HASH** at <https://my.telegram.org/apps>
>
> Get the **BOT_TOKEN** at <https://t.me/BotFather>

| Variable     | Description                                 |
| ------------ | ------------------------------------------- |
| API_ID       | Telegram api id                             |
| API_HASH     | Telegram api hash                           |
| BOT_TOKEN    | Token of you bot                            |
| ADMIN_ID     | User with admin privilegies (ex: Bot owner) |
| BOT_SESSION  | Bot session string to use in production     |
| USER_SESSION | User session string to use in production    |

## Bot

### Bot Requirements

- [x] Multi languages
- [ ] Configuration per user
- [ ] Watch channels configured by users and forward to the user the message that match with them filter
- [ ] All commands start an action and only can to finish completing it action or with `/cancel` command
- [ ] Allow cancel an action withh `/cancel` command
- Each user can:
  - [ ] Get all channels
  - [ ] Add channels to watch
  - [ ] Delete channels
  - [ ] Get all filters
  - [ ] Get all filters per channel
  - [ ] Add filters or keyword to a specific channel
  - [ ] Delete filters
- Admin can:
  - [x] List invited users
  - [x] Invite a new user using username
  - [x] Delete a user invitation using username
  - [x] List users registered
  - [x] Delete a user registered using ID

### Bot Commands

All users

- [x] Start (start)
- [x] Help (help)
- [ ] Cancel (cancel)
- [ ] Get all channels (list_channels)
- [ ] Add channel (add_channel)
- [ ] Delete channel (delete_channel)
- [ ] Get all filters (list_filters)
- [ ] Get all filters per channel (list_channel_filters)
- [ ] Add filter (add_filter)
- [ ] Delete filter (delete_filter)

Admins

- [x] List invited (invited)
- [x] Invite (invite \<username>)
- [x] Delete invitation (uninvite \<username>)
- [x] List users (list_users)
- [x] Delete user (delete_user \<id>)

## User bot

### User bot Requirements

- [ ] Join to channels configured per user
- [ ] Leave of channels that dont have users watching
- [ ] Watch channels configured and send messages that match with its filters to user that configured it
