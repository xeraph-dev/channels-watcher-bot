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

The clients implementation try to use **BOT_SESSION** and **USER_SESSION** variables, otherwise, it use **API_ID**, **API_HASH**, and **BOT_TOKEN** variables.

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

### Development

In dev mode, I recommend use nodemon to restart the command automatically

Start dev bot

```shell
yarn nodemon main.py
```

Watch prisma schema and regenerate if it change. _Tthis prisma executable was installed by python pip_

```shell
prisma generate --watch
```

Open prisma studio. _Using prisma installed by node.js (npm, yarn, pnpm, ...)_

```shell
yarn prisma studio
```

If the schema change, update the database with the current schema. _Tthis prisma executable was installed by python pip_

```shell
prisma db push
```

## Environment variables

> Get the **API_ID** and **API_HASH** at <https://my.telegram.org/apps>
>
> Get the **BOT_TOKEN** at <https://t.me/BotFather>

| Variable     | Description                              |
| ------------ | ---------------------------------------- |
| API_ID       | Telegram api id                          |
| API_HASH     | Telegram api hash                        |
| BOT_TOKEN    | Token of you bot                         |
| BOT_SESSION  | Bot session string to use in production  |
| USER_SESSION | User session string to use in production |

## Bot

### Bot Requirements

- [x] Multi languages
- [ ] Configuration per user
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
  - [x] List accepted users
  - [x] List users registered
  - [x] Delete a user registered using ID

### Bot Commands

All users

- [x] Help (help)
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
- [x] List acceted (accepted)
- [x] List users (list_users)
- [x] Delete user (delete_user \<id>)

## User bot

### User bot Requirements

- [ ] Join to channels configured per user
- [ ] Leave of channels that dont have users watching
- [ ] Watch channels configured and send messages that match with its filters to user that configured it
