from typing import Dict


class ServerContext:
    def __init__(self, guild_id: int, forwardLookup: Dict[str, int], reverseLookup: Dict[int, str]):
        self.GUILD_ID = guild_id
        self.fwl: Dict[str, int] = forwardLookup
        self.revL: Dict[int, str] = reverseLookup

    def channelToID(self, channel_name: str) -> int:
        if channel_name not in self.fwl:
            print("tried to lookup unknown: %s" % self.fwl)
            return self.fwl["conf"]
        else:
            return self.fwl[channel_name]

    def idToChannel(self, disc_id: int):
        if disc_id not in self.revL:
            print("invalid source channel: %s" % disc_id)
            return ""
        else:
            return self.revL[disc_id]


GUILD_ID = 783155485577707531  # Guild ID MUST be an int, not a string!

REGULAR_CONFESSION = 803443271023591425  # Channel ID MUST be an int, not a string!
ALT_CONFESSION = 803459487477923851  # Alt confession id (conf-redirect-2) on beta server
channel_to_id = {
    "conf": REGULAR_CONFESSION,
    "alt": ALT_CONFESSION
}
channels_nicks = {
    REGULAR_CONFESSION: "conf",
    ALT_CONFESSION: "alt"
}

# export #1
betaTest = ServerContext(GUILD_ID, channel_to_id, channels_nicks)

GUILD_ID = 754805686306603058  # Guild ID MUST be an int, not a string!

CONFESSIONS_ID = 755548197157339146  # truffles-confession-booth, !conf
VENT6_ID = 754823615504973855  # vent6-rise-of-the-bagel-bites, !vent
VC_CHAT_ID = 754807220448919642  # vc-chat-3, !vc
HORNY_ID = 755555065988644886  # horny, !horny
TIKTOK_ID = 791754062894333973  # tiktoks, !tiktok
MEMES_ID = 754889806080901150  # memes, !meme
RECOMMENDATIONS_ID = 783152680503738368  # recommendations, !rec
GAY_ID = 771063034714128416  # gay, !gay
chl_to_id = {
    "conf": CONFESSIONS_ID,
    "vent": VENT6_ID,
    "vc": VC_CHAT_ID,
    "horny": HORNY_ID,
    "tiktok": TIKTOK_ID,
    "meme": MEMES_ID,
    "rec": RECOMMENDATIONS_ID,
    "gay": GAY_ID
}

id_to_chl = {
    a[1]: a[0] for a in chl_to_id.items()
}

titsConfig = ServerContext(GUILD_ID, chl_to_id, id_to_chl)