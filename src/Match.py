#https://dota2api.readthedocs.io/en/latest/responses.html#towers-and-barracks

#tower status
# 1	ANCIENT TOP	1	Alive
# 2	ANCIENT BOTTOM	0
# 3	TOP 3		1	Alive
# 4	TOP 2		0
# 5	TOP 1		0
# 6	MIDDLE 3	1	Alive
# 7	MIDDLE 2	1	Alive
# 8	MIDDLE 1	1	Alive
# 9	BOTTOM 3	0
# 10	BOTTOM 2	0
# 11	BOTTOM 1	0

#game mode
# Value	Description
# 0	None
# 1	All Pick
# 2	Captain’s Mode
# 3	Random Draft
# 4	Single Draft
# 5	All Random
# 6	Intro
# 7	Diretide
# 8	Reverse Captain’s Mode
# 9	The Greeviling
# 10	Tutorial
# 11	Mid Only
# 12	Least Played
# 13	New Player Pool
# 14	Compendium Matchmaking
# 16	Captains Draft

#lobby type
# -1	invalid
# 0	Public matchmaking
# 1	Practice
# 2	Tournament
# 3	Tutorial
# 4	Co-op with AI
# 5	Team match
# 6	Solo queue
# 7	Ranked matchmaking
# 8	1v1 solo mid

# {
#     season                  - Season the game was played in
#     radiant_win             - Win status of game (True for Radiant win, False for Dire win)
#     duration                - Elapsed match time in seconds
#     start_time              - Unix timestamp for beginning of match
#     match_id                - Unique match ID
#     match_seq_num           - Number indicating position in which this match was recorded
#     tower_status_radiant    - Status of Radiant towers
#     tower_status_dire       - Status of Dire towers
#     barracks_status_radiant - Status of Radiant barracks
#     barracks_status_dire    - Status of Dire barracks
#     cluster                 - The server cluster the match was played on, used in retrieving replays
#     cluster_name            - ?
#     first_blood_time        - Time elapsed in seconds since first blood of the match
#     lobby_type              - See lobby_type table
#     lobby_name              - See lobby_type table
#     human_players           - Number of human players in the match
#     leagueid                - Unique league ID
#     positive_votes          - Number of positive/thumbs up votes
#     negative_votes          - Number of negative/thumbs down votes
#     game_mode               - See game_mode table
#     game_mode_name          - See game_mode table
#     radiant_captain         - account ID for Radiant captain
#     dire_captain            - account ID for Dire captain
#     [pick_bans]
#     {
#         {
#             hero_id         - Unique hero ID
#             is_pick         - True if hero was picked, False if hero was banned
#             order           - Order of pick or ban in overall pick/ban sequence
#             team            - See team_id table.

#         }
#     }
#     [players]
#     {
#         account_id          - Unique account ID
#         player_slot         - Player's position within the team
#         hero_id             - Unique hero ID
#         hero_name           - Hero's name
#         item_#              - Item ID for item in slot # (0-5)
#         item_#_name         - Item name for item in slot # (0-5)
#         kills               - Number of kills by player
#         deaths              - Number of player deaths
#         assists             - Number of player assists
#         leaver_status       - Connection/leaving status of player
#         gold                - Gold held by player
#         last_hits           - Number of last hits by player (creep score)
#         denies              - Number of denies
#         gold_per_min        - Average gold per minute
#         xp_per_min          - Average XP per minute
#         gold_spent          - Total amount of gold spent
#         hero_damage         - Amount of hero damage dealt by player
#         tower_damage        - Amount of tower damage dealt by player
#         hero_healing        - Amount of healing done by player
#         level               - Level of player's hero
#         [ability_upgrades]  - Order of abilities chosen by player
#         {
#             ability         - Ability chosen
#             time            - Time in seconds since match start when ability was upgraded
#             level           - Level of player at time of upgrading
#         }

#         [additional_units]  - Only available if the player has a additional unit
#         {
#             unitname        - Name of unit
#             item_#          - ID of item in slot # (0-5)
#         }
#     }
#     // These fields are only available for matches with teams //
#     [radiant_team]
#     {
#         team_name            - team name for Radiant
#         team_logo            - team logo for Radiant
#         team_complete   - ?
#     }
#     [dire_team]
#     {
#         team_name               - team name for Dire
#         team_logo               - team logo for Dire
#         team_team_complete      - ?
#     }
# }

import json as js
test = '{"tower_status_radiant":1972,"leagueid":0,"lobby_type":0,"radiant_win":true,"first_blood_time":8,"engine":1,"match_id":2281751941,"duration":2472,"barracks_status_radiant":63,"start_time":1460155879,"barracks_status_dire":0,"pre_game_duration":0,"game_mode":1,"positive_votes":0,"flags":0,"tower_status_dire":0,"cluster":204,"dire_score":30,"radiant_score":49,"match_seq_num":2000000001,"negative_votes":0,"human_players":10,"players":[{"account_id":4294967295,"scaled_tower_damage":0,"ability_upgrades":[{"ability":5122,"time":139,"level":1},{"ability":5123,"time":254,"level":2},{"ability":5123,"time":296,"level":3},{"ability":5122,"time":395,"level":4},{"ability":5122,"time":501,"level":5},{"ability":5125,"time":588,"level":6},{"ability":5124,"time":661,"level":7},{"ability":5124,"time":857,"level":8},{"ability":5123,"time":1007,"level":9},{"ability":5123,"time":1128,"level":10},{"ability":5124,"time":1313,"level":11},{"ability":5122,"time":1667,"level":12},{"ability":5124,"time":1722,"level":13},{"ability":5125,"time":1808,"level":14},{"ability":5002,"time":1960,"level":15},{"ability":5125,"time":2122,"level":16},{"ability":5002,"time":2328,"level":17},{"ability":5002,"time":2578,"level":18}],"item_2":229,"item_1":63,"assists":15,"item_5":0,"scaled_hero_healing":0,"gold_spent":13610,"player_slot":0,"hero_id":20,"level":19,"item_4":154,"leaver_status":0,"item_3":168,"gold":3055,"kills":5,"denies":12,"deaths":8,"hero_healing":0,"hero_damage":7050,"last_hits":132,"gold_per_min":436,"tower_damage":2856,"item_0":46,"scaled_hero_damage":0,"xp_per_min":479},{"account_id":4294967295,"scaled_tower_damage":0,"ability_upgrades":[{"ability":5263,"time":202,"level":1},{"ability":5264,"time":306,"level":2},{"ability":5263,"time":384,"level":3},{"ability":5265,"time":519,"level":4},{"ability":5265,"time":613,"level":5},{"ability":5266,"time":735,"level":6},{"ability":5264,"time":872,"level":7},{"ability":5263,"time":947,"level":8},{"ability":5263,"time":1305,"level":9},{"ability":5265,"time":1531,"level":10},{"ability":5266,"time":1598,"level":11},{"ability":5264,"time":1807,"level":12},{"ability":5265,"time":2062,"level":13},{"ability":5264,"time":2121,"level":14},{"ability":5002,"time":2318,"level":15},{"ability":5266,"time":2453,"level":16},{"ability":5002,"time":2520,"level":17},{"ability":5002,"time":2578,"level":18}],"item_2":231,"item_1":88,"assists":29,"item_5":0,"scaled_hero_healing":0,"gold_spent":10025,"player_slot":1,"hero_id":57,"level":19,"item_4":0,"leaver_status":0,"item_3":0,"gold":5659,"kills":2,"denies":3,"deaths":3,"hero_healing":5492,"hero_damage":5572,"last_hits":45,"gold_per_min":380,"tower_damage":461,"item_0":100,"scaled_hero_damage":0,"xp_per_min":483},{"account_id":184333528,"scaled_tower_damage":0,"ability_upgrades":[{"ability":5090,"time":136,"level":1},{"ability":5685,"time":321,"level":2},{"ability":5090,"time":393,"level":3},{"ability":5685,"time":483,"level":4},{"ability":5090,"time":624,"level":5},{"ability":5093,"time":779,"level":6},{"ability":5091,"time":944,"level":7},{"ability":5685,"time":1024,"level":8},{"ability":5090,"time":1406,"level":9},{"ability":5093,"time":1531,"level":10},{"ability":5685,"time":1532,"level":11},{"ability":5091,"time":1721,"level":12},{"ability":5091,"time":1721,"level":13},{"ability":5091,"time":1811,"level":14},{"ability":5002,"time":1983,"level":15},{"ability":5093,"time":2159,"level":16},{"ability":5002,"time":2277,"level":17},{"ability":5002,"time":2456,"level":18},{"ability":5002,"time":2456,"level":19},{"ability":5002,"time":2584,"level":20}],"item_2":206,"item_1":48,"assists":20,"item_5":0,"scaled_hero_healing":0,"gold_spent":22950,"player_slot":2,"hero_id":43,"level":20,"item_4":160,"leaver_status":0,"item_3":121,"gold":261,"kills":9,"denies":7,"deaths":6,"hero_healing":0,"hero_damage":19741,"last_hits":141,"gold_per_min":531,"tower_damage":4246,"item_0":152,"scaled_hero_damage":0,"xp_per_min":535},{"account_id":103053437,"scaled_tower_damage":0,"ability_upgrades":[{"ability":5023,"time":176,"level":1},{"ability":5024,"time":288,"level":2},{"ability":5023,"time":362,"level":3},{"ability":5025,"time":471,"level":4},{"ability":5023,"time":653,"level":5},{"ability":5026,"time":931,"level":6},{"ability":5023,"time":1066,"level":7},{"ability":5024,"time":1160,"level":8},{"ability":5024,"time":1401,"level":9},{"ability":5025,"time":1531,"level":10},{"ability":5026,"time":1546,"level":11},{"ability":5024,"time":1721,"level":12},{"ability":5025,"time":1806,"level":13},{"ability":5025,"time":1948,"level":14},{"ability":5002,"time":2081,"level":15},{"ability":5026,"time":2134,"level":16},{"ability":5002,"time":2343,"level":17}],"item_2":108,"item_1":190,"assists":21,"item_5":180,"scaled_hero_healing":0,"gold_spent":16150,"player_slot":3,"hero_id":7,"level":17,"item_4":0,"leaver_status":0,"item_3":119,"gold":746,"kills":9,"denies":0,"deaths":11,"hero_healing":0,"hero_damage":14494,"last_hits":79,"gold_per_min":447,"tower_damage":321,"item_0":1,"scaled_hero_damage":0,"xp_per_min":399},{"account_id":103925764,"scaled_tower_damage":0,"ability_upgrades":[{"ability":5495,"time":244,"level":1},{"ability":5494,"time":284,"level":2},{"ability":5495,"time":376,"level":3},{"ability":5494,"time":501,"level":4},{"ability":5495,"time":662,"level":5},{"ability":5497,"time":789,"level":6},{"ability":5495,"time":829,"level":7},{"ability":5494,"time":847,"level":8},{"ability":5494,"time":1004,"level":9},{"ability":5496,"time":1146,"level":10},{"ability":5497,"time":1232,"level":11},{"ability":5496,"time":1668,"level":12},{"ability":5496,"time":1736,"level":13},{"ability":5496,"time":1817,"level":14},{"ability":5002,"time":1945,"level":15},{"ability":5497,"time":2064,"level":16},{"ability":5002,"time":2130,"level":17},{"ability":5002,"time":2253,"level":18},{"ability":5002,"time":2260,"level":19},{"ability":5002,"time":2292,"level":20},{"ability":5002,"time":2459,"level":21},{"ability":5002,"time":2588,"level":22},{"ability":5002,"time":2590,"level":23}],"item_2":160,"item_1":152,"assists":19,"item_5":37,"scaled_hero_healing":0,"gold_spent":21325,"player_slot":4,"hero_id":93,"level":24,"item_4":139,"leaver_status":0,"item_3":143,"gold":4244,"kills":24,"denies":0,"deaths":2,"hero_healing":0,"hero_damage":30975,"last_hits":95,"gold_per_min":603,"tower_damage":4397,"item_0":63,"scaled_hero_damage":0,"xp_per_min":767},{"account_id":4294967295,"scaled_tower_damage":0,"ability_upgrades":[{"ability":5052,"time":158,"level":1},{"ability":5053,"time":248,"level":2},{"ability":5056,"time":312,"level":3},{"ability":5055,"time":356,"level":4},{"ability":5056,"time":424,"level":5},{"ability":5052,"time":498,"level":6},{"ability":5053,"time":562,"level":7},{"ability":5057,"time":635,"level":8},{"ability":5055,"time":812,"level":9},{"ability":5053,"time":1032,"level":10},{"ability":5052,"time":1112,"level":11},{"ability":5053,"time":1324,"level":12},{"ability":5052,"time":1425,"level":13},{"ability":5057,"time":1476,"level":14},{"ability":5002,"time":1606,"level":15},{"ability":5057,"time":1779,"level":16},{"ability":5002,"time":2147,"level":17},{"ability":5002,"time":2213,"level":18},{"ability":5002,"time":2446,"level":19}],"item_2":37,"item_1":123,"assists":7,"item_5":164,"scaled_hero_healing":0,"gold_spent":12750,"player_slot":128,"hero_id":10,"level":19,"item_4":212,"leaver_status":0,"item_3":63,"gold":2191,"kills":5,"denies":2,"deaths":7,"hero_healing":0,"hero_damage":9465,"last_hits":191,"gold_per_min":389,"tower_damage":1276,"item_0":41,"scaled_hero_damage":0,"xp_per_min":500},{"account_id":4294967295,"scaled_tower_damage":0,"ability_upgrades":[{"ability":5595,"time":184,"level":1},{"ability":5596,"time":283,"level":2},{"ability":5597,"time":419,"level":3},{"ability":5596,"time":511,"level":4},{"ability":5597,"time":656,"level":5},{"ability":5598,"time":845,"level":6},{"ability":5596,"time":938,"level":7},{"ability":5597,"time":1098,"level":8},{"ability":5596,"time":1189,"level":9},{"ability":5597,"time":1348,"level":10},{"ability":5598,"time":1455,"level":11},{"ability":5595,"time":1617,"level":12},{"ability":5595,"time":1720,"level":13},{"ability":5595,"time":1902,"level":14},{"ability":5002,"time":2120,"level":15},{"ability":5598,"time":2225,"level":16}],"item_2":1,"item_1":127,"assists":13,"item_5":8,"scaled_hero_healing":0,"gold_spent":10455,"player_slot":129,"hero_id":104,"level":16,"item_4":63,"leaver_status":0,"item_3":212,"gold":68,"kills":5,"denies":3,"deaths":10,"hero_healing":0,"hero_damage":11595,"last_hits":101,"gold_per_min":304,"tower_damage":215,"item_0":36,"scaled_hero_damage":0,"xp_per_min":355},{"account_id":4294967295,"scaled_tower_damage":0,"ability_upgrades":[{"ability":5094,"time":130,"level":1},{"ability":5096,"time":251,"level":2},{"ability":5094,"time":345,"level":3},{"ability":5095,"time":440,"level":4},{"ability":5094,"time":582,"level":5},{"ability":5097,"time":690,"level":6},{"ability":5094,"time":774,"level":7},{"ability":5095,"time":840,"level":8},{"ability":5096,"time":1051,"level":9},{"ability":5095,"time":1178,"level":10},{"ability":5097,"time":1216,"level":11},{"ability":5095,"time":1445,"level":12},{"ability":5096,"time":1617,"level":13},{"ability":5096,"time":1795,"level":14},{"ability":5002,"time":1973,"level":15},{"ability":5097,"time":2208,"level":16},{"ability":5002,"time":2229,"level":17},{"ability":5002,"time":2443,"level":18},{"ability":5002,"time":2625,"level":19}],"item_2":1,"item_1":170,"assists":9,"item_5":63,"scaled_hero_healing":0,"gold_spent":12685,"player_slot":130,"hero_id":18,"level":19,"item_4":46,"leaver_status":0,"item_3":116,"gold":961,"kills":10,"denies":7,"deaths":8,"hero_healing":0,"hero_damage":15127,"last_hits":172,"gold_per_min":415,"tower_damage":125,"item_0":164,"scaled_hero_damage":0,"xp_per_min":503},{"account_id":4294967295,"scaled_tower_damage":0,"ability_upgrades":[{"ability":5163,"time":230,"level":1},{"ability":5162,"time":284,"level":2},{"ability":5163,"time":369,"level":3},{"ability":5162,"time":455,"level":4},{"ability":5163,"time":635,"level":5},{"ability":5165,"time":831,"level":6},{"ability":5163,"time":1040,"level":7},{"ability":5162,"time":1263,"level":8},{"ability":5162,"time":1452,"level":9},{"ability":5164,"time":1660,"level":10},{"ability":5165,"time":1858,"level":11},{"ability":5164,"time":2340,"level":12},{"ability":5164,"time":2462,"level":13},{"ability":5164,"time":2669,"level":14}],"item_2":36,"item_1":1,"assists":11,"item_5":21,"scaled_hero_healing":0,"gold_spent":9340,"player_slot":131,"hero_id":37,"level":14,"item_4":73,"leaver_status":0,"item_3":181,"gold":615,"kills":3,"denies":6,"deaths":13,"hero_healing":761,"hero_damage":9782,"last_hits":62,"gold_per_min":283,"tower_damage":376,"item_0":180,"scaled_hero_damage":0,"xp_per_min":285},{"account_id":4294967295,"scaled_tower_damage":0,"ability_upgrades":[{"ability":5299,"time":196,"level":1},{"ability":5298,"time":280,"level":2},{"ability":5297,"time":396,"level":3},{"ability":5297,"time":439,"level":4},{"ability":5298,"time":579,"level":5},{"ability":5300,"time":669,"level":6},{"ability":5298,"time":816,"level":7},{"ability":5297,"time":902,"level":8},{"ability":5298,"time":1234,"level":9},{"ability":5297,"time":1365,"level":10},{"ability":5300,"time":1412,"level":11},{"ability":5299,"time":1841,"level":12},{"ability":5299,"time":1842,"level":13},{"ability":5299,"time":1989,"level":14},{"ability":5002,"time":2200,"level":15},{"ability":5300,"time":2513,"level":16}],"item_2":43,"item_1":79,"assists":14,"item_5":0,"scaled_hero_healing":0,"gold_spent":8175,"player_slot":132,"hero_id":64,"level":16,"item_4":0,"leaver_status":0,"item_3":100,"gold":1035,"kills":6,"denies":1,"deaths":11,"hero_healing":1202,"hero_damage":15815,"last_hits":90,"gold_per_min":309,"tower_damage":366,"item_0":180,"scaled_hero_damage":0,"xp_per_min":366}]}'


class Match:
	def __init__(matchJSON):

		jMatch = js.loads(matchJSON)
#     season                  - Season the game was played in
#     radiant_win             - Win status of game (True for Radiant win, False for Dire win)
#     duration                - Elapsed match time in seconds
#     start_time              - Unix timestamp for beginning of match
#     match_id                - Unique match ID
#     match_seq_num           - Number indicating position in which this match was recorded
#     tower_status_radiant    - Status of Radiant towers
#     tower_status_dire       - Status of Dire towers
#     barracks_status_radiant - Status of Radiant barracks
#     barracks_status_dire    - Status of Dire barracks
#     cluster                 - The server cluster the match was played on, used in retrieving replays
#     cluster_name            - ?
#     first_blood_time        - Time elapsed in seconds since first blood of the match
#     lobby_type              - See lobby_type table
#     lobby_name              - See lobby_type table
#     human_players           - Number of human players in the match
#     leagueid                - Unique league ID
#     positive_votes          - Number of positive/thumbs up votes
#     negative_votes          - Number of negative/thumbs down votes
#     game_mode               - See game_mode table
#     game_mode_name          - See game_mode table
#     radiant_captain         - account ID for Radiant captain
#     dire_captain            - account ID for Dire captain
	self.season = jMatch['season']
	self.radiant_win = jMatch['radiant_win']

	print(self.season)
	print(self.radiant_win)

