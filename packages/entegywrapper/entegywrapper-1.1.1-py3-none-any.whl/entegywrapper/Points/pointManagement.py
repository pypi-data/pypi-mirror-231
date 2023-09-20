from entegywrapper.schemas.points import LeaderboardPosition, PointType


def award_points(
    self,
    point_type: PointType,
    points: int,
    *,
    profile_id: str | None = None,
    external_reference: str | None = None,
    badge_reference: str | None = None,
    internal_reference: str | None = None,
):
    """
    Awards the given number of points to the specified profile.

    Parameters
    ----------
        `point_type` (`PointType`): the type of points to assign
        `points` (`int`): the amount of points to assign
        `profile_id` (`str`, optional): the profileId for the profile; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`
        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`
        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
    """
    data = {
        "pointEvent": point_type,
        "points": points
    }

    if profile_id is not None:
        data["profileId"] = profile_id
    elif external_reference is not None:
        data["externalReference"] = profile_id
    elif badge_reference is not None:
        data["badgeReference"] = profile_id
    elif internal_reference is not None:
        data["internalReference"] = profile_id
    else:
        raise ValueError("Please specify an identifier")

    self.post(
        self.api_endpoint + "/v2/Point/Award",
        headers=self.headers,
        data=data
    )


def get_points(
    self,
    *,
    profile_id: str | None = None,
    external_reference: str | None = None,
    badge_reference: str | None = None,
    internal_reference: str | None = None
) -> int:
    """
    Returns the amount of points the specified profile has.

    Parameters
    ----------
        `profile_id` (`str`, optional): the profileId for the profile; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the profile; defaults to `None`
        `badge_reference` (`str`, optional): the badgeReference of the profile; defaults to `None`
        `internal_reference` (`str`, optional): the internalReference of the profile; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified

    Returns
    -------
        `int`: the amount of points the specified profile has
    """
    data = {}

    if profile_id is not None:
        data["profileId"] = profile_id
    elif external_reference is not None:
        data["externalReference"] = profile_id
    elif badge_reference is not None:
        data["badgeReference"] = profile_id
    elif internal_reference is not None:
        data["internalReference"] = profile_id
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(
        self.api_endpoint + "/v2/Point/Earned",
        headers=self.headers,
        data=data
    )

    return response["points"]


def get_point_leaderboard(self) -> list[LeaderboardPosition]:
    """
    Returns the leaderboard for the project. The response is sorted by the
    profiles response and includes their position with ties correctly handled.

    Returns
    -------
        `list[LeaderboardPosition]`: the leaderboard position for each profile
    """
    data = {}

    response = self.post(
        self.api_endpoint + "/v2/Point/Leaderboard",
        headers=self.headers,
        data=data
    )

    return response["leaderboard"]
