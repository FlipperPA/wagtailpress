@register.assignment_tag(takes_context=True)
def get_site_root(context):
	"""
	Gets the root page for the site. Returns a wagtailcore.Page model.
	"""

    return context['request'].site.root_page


def has_menu_children(page):
	"""
	Returns a boolean for whether or not the current page has child pages.
	"""

    return page.get_children().live().in_menu().exists()


@register.inclusion_tag('wagtailpress/tags/nav.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    """
    Retrieves the top menu items - the immediate children of the parent page
    The has_menu_children method is necessary because the bootstrap menu requires
    a dropdown class to be applied to a parent
    """

    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }