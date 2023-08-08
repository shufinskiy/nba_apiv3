from nba_apiv3.stats.static import teams


def test_get_request_url():
    assert len(teams.teams) == 30
