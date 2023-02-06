from models.Player import Player
from discord import Embed, Color


def generate_player_info_embed(player: Player):
    embed = Embed(title=player.name, description="General info", color=Color.blue())

    embed.add_field(name="Attack wins", value=str(player.attack_wins))
    embed.add_field(name="Defense wins", value=str(player.defense_wins))
    embed.add_field(name="Town hall level", value=str(player.town_hall_level))
    embed.add_field(name="Versus battle wins", value=str(player.versus_battle_wins))
    embed.add_field(name="Donations", value=str(player.donations))
    embed.add_field(name="Donations recieved", value=str(player.donations_recieved))
    embed.add_field(
        name="Clan capital contributions", value=str(player.clan_capital_contributions)
    )

    return embed
