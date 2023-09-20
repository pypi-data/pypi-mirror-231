from entegywrapper.errors import EntegyFailedRequestError
from entegywrapper.schemas.content import Category, TemplateType


def available_categories(
    self,
    template_type: TemplateType,
    *,
    module_id: int | None = None,
    external_reference: str | None = None,
) -> list[Category]:
    """
    Returns the list of available categories for the page specified by the given
    identifier.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page
        `module_id` (`int`, optional): the moduleId of the page; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
        `EntegyFailedRequestError`: if the API request fails

    Returns
    -------
        `list[Category]`: the available categories
    """
    data = {"templateType": template_type}

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/Categories/Available", data=data)

    match response["response"]:
        case 200:
            return response["availableCategories"]
        case 401:
            raise EntegyFailedRequestError("Missing Id")
        case 402:
            raise EntegyFailedRequestError("templateType doesn't support categories")
        case _:
            raise EntegyFailedRequestError("Unknown error")


def select_categories(
    self,
    template_type: TemplateType,
    categories: list[Category],
    *,
    module_id: int | None = None,
    external_reference: str | None = None,
) -> bool:
    """
    Selects the specified categories for the specified content page.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page selecting the categories
        `categories` (`list[Category]`): the categories to select
        `module_id` (`int`, optional): the moduleId of the page selecting the categories; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page selecting the categories; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
        `EntegyFailedRequestError`: if the API request fails

    Returns
    -------
        `bool`: whether the categories were selected successfully
    """
    data = {"templateType": template_type, "categories": categories}

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/Categories/Select", data=data)

    match response["response"]:
        case 200:
            return
        case 401:
            raise EntegyFailedRequestError("Missing Id")
        case 402:
            raise EntegyFailedRequestError("templateType doesn't support categories")
        case 404:
            raise EntegyFailedRequestError("No categories")
        case _:
            raise EntegyFailedRequestError("Unknown error")


def deselect_categories(
    self,
    template_type: TemplateType,
    categories: list[Category],
    *,
    module_id: int | None = None,
    external_reference: str | None = None,
) -> bool:
    """
    Deselects the specified categories for the specified content page.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page to unselect the categories from
        `categories` (`list[Category]`): the categories to select
        `module_id` (`int`, optional): the moduleId of the page to unselect the categories from; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page to unselect the categories from; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
        `EntegyFailedRequestError`: if the API request fails

    Returns
    -------
        `bool`: whether the categories were deselected successfully
    """
    data = {"templateType": template_type, "categories": categories}

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/Categories/Deselect", data=data)

    match response["response"]:
        case 200:
            return
        case 401:
            raise EntegyFailedRequestError("Missing Id")
        case 402:
            raise EntegyFailedRequestError("templateType doesn't support categories")
        case 404:
            raise EntegyFailedRequestError("Category doesn't exist")
        case 405:
            raise EntegyFailedRequestError("Category not selected")
        case 406:
            raise EntegyFailedRequestError("No categories to unselect")
        case _:
            raise EntegyFailedRequestError("Unknown error")


def create_categories(
    self,
    template_type: TemplateType,
    categories: list[Category],
    *,
    module_id: int | None = None,
    external_reference: str | None = None,
):
    """
    Creates categories under a root page.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page holding the categories
        `categories` (`list[Category]`): the categories to create
        `module_id` (`int`, optional): the moduleId of the page holding the categories; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page holding the categories; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
        `EntegyFailedRequestError`: if the API request fails
    """
    data = {"templateType": template_type, "categories": categories}

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/Categories/Create", data=data)

    match response["response"]:
        case 200:
            return
        case 401:
            raise EntegyFailedRequestError("Missing Id")
        case 402:
            raise EntegyFailedRequestError("Can't create categories here")
        case 404:
            raise EntegyFailedRequestError("Duplicate externalReference")
        case 405:
            raise EntegyFailedRequestError("Missing name")
        case _:
            raise EntegyFailedRequestError("Unknown error")


def create_child_categories(
    self,
    categories: list[Category],
    *,
    module_id: int | None = None,
    external_reference: str | None = None,
):
    """
    Creates categories under another category.

    Parameters
    ----------
        `categories` (`list[Category]`): the categories to create
        `module_id` (`int`): the moduleId of the page holding the categories
        `external_reference` (`int`): the externalReference of the page holding the categories

    Raises
    ------
        `ValueError`: if no identifier is specified
        `EntegyFailedRequestError`: if the API request fails
    """
    data = {"categories": categories}

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/Categories/CreateChild", data=data)

    match response["response"]:
        case 200:
            return
        case 401:
            raise EntegyFailedRequestError("Missing Id")
        case 404:
            raise EntegyFailedRequestError("Duplicate externalReference")
        case 405:
            raise EntegyFailedRequestError("Missing name")
        case _:
            raise EntegyFailedRequestError("Unknown error")


def update_category(
    self,
    name: str,
    *,
    module_id: int | None = None,
    external_reference: str | None = None,
):
    """
    Changes the name of a category.

    Parameters
    ----------
        `name` (`str`): the new name of the category
        `module_id` (`int`, optional): the moduleId of the category; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the category; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
        `EntegyFailedRequestError`: if the API request fails
    """
    data = {"name": name}

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.post(self.api_endpoint + "/v2/Categories/Update", data=data)

    match response["response"]:
        case 200:
            return
        case 401:
            raise EntegyFailedRequestError("Missing Id")
        case 402:
            raise EntegyFailedRequestError("Missing name")
        case _:
            raise EntegyFailedRequestError("Unknown error")


def delete_categories(
    self,
    template_type: TemplateType,
    categories: list[Category],
    *,
    module_id: int | None = None,
    external_reference: str | None = None,
):
    """
    Creates categories under another category.

    Parameters
    ----------
        `template_type` (`TemplateType`): the templateType of the page
        `categories` (`list[Category]`): the categories to delete
        `module_id` (`int`, optional): the moduleId of the page; defaults to `None`
        `external_reference` (`str`, optional): the externalReference of the page; defaults to `None`

    Raises
    ------
        `ValueError`: if no identifier is specified
        `EntegyFailedRequestError`: if the API request fails
    """
    data = {"templateType": template_type, "categories": categories}

    if module_id is not None:
        data["moduleId"] = module_id
    elif external_reference is not None:
        data["externalReference"] = external_reference
    else:
        raise ValueError("Please specify an identifier")

    response = self.delete(self.api_endpoint + "/v2/Categories/Delete", data=data)

    match response["response"]:
        case 200:
            return
        case 401:
            raise EntegyFailedRequestError("Missing Id")
        case 404:
            raise EntegyFailedRequestError("Category doesn't exist")
        case _:
            raise EntegyFailedRequestError("Unknown error")
