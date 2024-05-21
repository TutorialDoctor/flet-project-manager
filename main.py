from flet import *

def main(page: Page):
    # SETUP
    page.title = "Todo App"
    page.window_width = 1800
    page.window_height = 1200
    page.theme_mode = ThemeMode.LIGHT
    SLATE_100 = "#f1f5f9"
    SLATE_200 = "#e2e8f09"
    page.padding = 10
    page.bgcolor = SLATE_100
    LOGO_URL = "https://static-00.iconduck.com/assets.00/todo-icon-1024x1024-8p9cd4g6.png"
    # END SETUP

    # ROUTING
    bar = NavigationBar(
        destinations=[
            NavigationDestination(icon=icons.EXPLORE, label="Home"),
            NavigationDestination(icon=icons.EXPLORE, label="Automations"),
            NavigationDestination(icon=icons.PIE_CHART_ROUNDED, label="Reports"),
            NavigationDestination(
                icon=icons.BOOKMARK_BORDER,
                selected_icon=icons.BOOKMARK,
                label="Store",
            ),
            NavigationDestination(icon=icons.ACCOUNT_TREE_OUTLINED, label="Projects"),
        ],
        on_change=lambda x: page.go(
            f"/{x.control.destinations[x.control.selected_index].label.lower()}"
        ),
    )

    def render(path,controls=[Text("Hi")]):
        if page.route == f"{path}":
           page.views.append(
               View(f'{path}',controls,bgcolor=SLATE_100)
           )

    def route_change(route):
        page.views.clear()

        render('/home',
            [
                AppBar(title=Text("Tasks"), bgcolor=colors.SURFACE_VARIANT),
                Row([sidebar(), main_area], vertical_alignment=CrossAxisAlignment.START),
                bar,
            ]
        )

        render('/store',[
            AppBar(title=Text("Store"), bgcolor=colors.SURFACE_VARIANT),
            sidebar(),
            ElevatedButton("Go Home", on_click=lambda _: page.go("/home")),
            bar,
        ])

        render('/projects',[
            AppBar(title=Text("Projects"), bgcolor=colors.SURFACE_VARIANT),
            navbar,
            sidebar(),
            ElevatedButton("Go Home", on_click=lambda _: page.go("/home")),
            bar,
        ])

        render('/automations',[
            AppBar(title=Text("Automations"), bgcolor=colors.SURFACE_VARIANT),
            sidebar(),
            GridView([Text("Automations Page")]),
            ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
            bar,
        ])

        render('/reports',[
            AppBar(title=Text("Reports"), bgcolor=colors.SURFACE_VARIANT),
            sidebar(),
            ElevatedButton("Go Home", on_click=lambda _: page.go("/reports")),
            bar,
        ])

        page.update()

    page.on_route_change = route_change
    page.go(page.route)
    page.go('/home')
    # END ROUTING

    # GUI
    navbar = Container(
        Row(
            [
                Row(
                    [
                        Image(
                            width=30,
                            height=30,
                            src=LOGO_URL,
                        ),
                        Text(page.title, color="#374151"),
                    ]
                ),
                Row(
                    [
                        CupertinoTextField("Search", bgcolor="#e2e8f0", color="black"),
                        ElevatedButton("Search", color="white", bgcolor="black"),
                        Text("About", color="#374151"),
                        Text("Contact", color="#374151"),
                        IconButton(icon=icons.SETTINGS_ROUNDED, icon_color="#111827"),
                    ]
                ),
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
        ),
        bgcolor="white",
        padding=10,
        border_radius=8,
    )

    def sidebar():
        return Container(
            Column(
                [
                    TextButton(
                        "Tasks", icon=icons.FACT_CHECK_OUTLINED, icon_color="black",
                        on_click = lambda x: page.go('/home')
                    ),
                    TextButton(
                        "Projects", icon=icons.ACCOUNT_TREE_OUTLINED, icon_color="black",on_click = lambda x: page.go('/projects')
                    ),
                    TextButton(
                        "Routine", icon=icons.OFFLINE_BOLT_OUTLINED, icon_color="black"
                    ),
                    TextButton(
                        "Notes", icon=icons.STICKY_NOTE_2_OUTLINED, icon_color="black"
                    ),
                    TextButton(
                        "Automations",
                        icon=icons.AUTO_AWESOME_OUTLINED,
                        icon_color="black",
                        on_click = lambda x: page.go('/automations')
                    ),
                    TextButton(
                        "Reports", icon=icons.PIE_CHART_ROUNDED, icon_color="black",
                        on_click = lambda x: page.go('/reports')
                    ),
                ],
                spacing=20,
            ),
            bgcolor="white",
            padding=16,
            border_radius=10,
        )

    task_list = {
        "name": "Linkedin",
        "timeline": "Sun 12/12 - Mon 1/13",
        "items": [
            {"completed": False, "label": "Dribble"},
            {"completed": False, "label": "Moodboard"},
            {"completed": False, "label": "App Exploration"},
            {"completed": False, "label": "Strategy Planning"},
        ],
    }

    design_task_list = {
        "name": "Landing",
        "timeline": "Sun 12/12 - Mon 1/13",
        "items": [
            {"completed": False, "label": "Wireframes"},
            {"completed": False, "label": "Mockups"},
            {"completed": False, "label": "User Experience"},
            {"completed": False, "label": "DB Design"},
        ],
    }

    design_task_list2 = {
        "name": "Dashboard",
        "timeline": "Sun 12/22 - Mon 1/24",
        "items": [
            {"completed": False, "label": "Wireframes"},
            {"completed": False, "label": "Mockups"},
            {"completed": False, "label": "User Experience"},
            {"completed": False, "label": "DB Design"},
        ],
    }

    dev_task_list = {
        "name": "Basic User",
        "timeline": "Sun 12/12 - Mon 1/13",
        "items": [
            {"completed": False, "label": "Frontend"},
            {"completed": False, "label": "API"},
            {"completed": False, "label": "DB Design"},
            {"completed": False, "label": "Backend"},
        ],
    }

    dev_task_list2 = {
        "name": "Admins",
        "timeline": "Sun 12/12 - Mon 1/13",
        "items": [
            {"completed": False, "label": "Frontend"},
            {"completed": False, "label": "API"},
            {"completed": False, "label": "DB Design"},
            {"completed": False, "label": "Backend"},
        ],
    }

    marketing_task_list = {
        "name": "Index",
        "timeline": "Sun 12/12 - Mon 1/13",
        "items": [
            {"completed": False, "label": "Website"},
            {"completed": False, "label": "Social Media"},
            {"completed": False, "label": "Analytics"},
            {"completed": False, "label": "Branding"},
        ],
    }

    sales_task_list = {
        "name": "Index",
        "timeline": "Sun 12/12 - Mon 1/13",
        "items": [
            {"completed": False, "label": "Cold Calling"},
            {"completed": False, "label": "Yearly Campaigns"},
            {"completed": False, "label": "Monthly Campaigns"},
            {"completed": False, "label": "Weekly Compaigns"},
        ],
    }

    def NewTaskList(tl=[]):
        task_list_component = Container(
            Column(
                [
                    Row(
                        [
                            Text(tl["name"], weight=FontWeight.W_500, size=16),
                        ],
                        alignment=MainAxisAlignment.START,
                    ),
                    Column(
                        [
                            Row(
                                [
                                    Checkbox(),
                                    Text(tl["items"][ndx]["label"]),
                                ] 
                            )
                            for ndx, task in enumerate(tl["items"])
                        ] + [dates(tl)]
                    ),
                ]
            ),
            bgcolor="white",
            padding=10,
            border_radius=10,
            width=200,
        )
        return task_list_component

    def dates(tl):
        return Row(
                            [
                                Container(
                                    Text(tl['timeline']),
                                    padding=8,
                                    border_radius=10,
                                    bgcolor="#e2e8f0",
                                ),
                            ]
                        )

    main_area = Container(
        Column(
            [
                navbar,
                Container(
                    Row([
                        Row([
                            IconButton(icons.ARROW_BACK_ROUNDED),
                            Text("Health Application for PHD Health")
                            ]),
                        ElevatedButton("Add Phase")
                    ],alignment=MainAxisAlignment.SPACE_BETWEEN),bgcolor='white',padding=10,border_radius=10
                ),
                ResponsiveRow(
                    [
                        Container(
                            Column(
                                [
                                    Container(
                                        Text("Research", color="white", width=160),
                                        padding=20,
                                        border_radius=6,
                                        bgcolor="purple",
                                    ),
                                    NewTaskList(task_list),
                                    NewTaskList(task_list),
                                ]
                            ),col={'sm':12,'lg':2}
                        ),
                        Container(
                            Column(
                                [
                                    Container(
                                        Text("Design", color="white", width=160),
                                        padding=20,
                                        border_radius=6,
                                        bgcolor="teal",
                                    ),
                                    NewTaskList(design_task_list),
                                    NewTaskList(design_task_list2),
                                ]
                            ),col={'sm':12,'lg':2}
                        ),
                        Container(
                            Column(
                                [
                                    Container(
                                        Text("Development", color="white", width=160),
                                        padding=20,
                                        border_radius=6,
                                        bgcolor="black",
                                    ),
                                    NewTaskList(dev_task_list),
                                    NewTaskList(dev_task_list2),
                                    NewTaskList(dev_task_list),
                                ]
                            ),col={'sm':12,'lg':2}
                        ),
                        Container(
                            Column(
                                [
                                    Container(
                                        Text("Marketing", color="white", width=160),
                                        padding=20,
                                        border_radius=6,
                                        bgcolor="orange",
                                    ),
                                    NewTaskList(marketing_task_list),
                                    NewTaskList(marketing_task_list),
                                ]
                            ),col={'sm':12,'lg':2}
                        ),
                        Container(
                            Column(
                                [
                                    Container(
                                        Text("Sales", color="white", width=160),
                                        padding=20,
                                        border_radius=6,
                                        bgcolor="red",
                                    ),
                                    NewTaskList(sales_task_list),
                                ]
                            ),col={'sm':12,'lg':2}
                        ),
                    ],
                    alignment=MainAxisAlignment.START,
                    vertical_alignment=CrossAxisAlignment.START,
                    spacing=20,
                )
            ]
        ),
        expand=True,
        bgcolor="#f1f5f9",
    )
    # END GUI

    # page.add(
    #     Row([sidebar(), main_area], vertical_alignment=CrossAxisAlignment.START)
    # )


app(target=main)
