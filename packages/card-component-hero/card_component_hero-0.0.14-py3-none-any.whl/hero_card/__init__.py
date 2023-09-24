import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _card_component = components.declare_component(
        "card_component",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _card_component = components.declare_component("card_component", path=build_dir)

def card_component(data=None, styles=None, typeExpand=None, showAdd=None, addHeroComponent=None, showHero=None, showChartSwitch=None, saveEdits=None, EditDashboard=None, userSetRating=None, key=None):
  
    component_value = _card_component(
        data=data, 
        styles=styles, 
        typeExpand=typeExpand, 
        showAdd=showAdd, 
        addHeroComponent=addHeroComponent, 
        showHero=showHero, 
        showChartSwitch=showChartSwitch, 
        saveEdits=saveEdits,
        EditDashboard=EditDashboard,
        userSetRating=userSetRating,
        key=key, 
        default=0
        )

    return component_value

if not _RELEASE:
    import streamlit as st

    st.set_page_config(layout="wide")

    data = [
        {
      "index": 0,
      "addNewHero":False,
      "toStore":False,
      "hasChanged":False,
      "remove":False,
      "confirmRemove":False,
      "clickedChange":False,
      "ratings":0,
      "numOfUsersRatedVal": 80,
      "indexName": "equipmentItems",
      "title": "Equipment name",
      "titleVal":"equipment name",
      "numOfHeroes": [
        {
          "index": 0,
          "sum": "+7",
          "expand": True,
         "heroesUserAttachedToSet": [ ]
        }
      ],
      "changeTitleBtnLayout":{"disabled":True},
      "changeTitleTxtF":{"value":"", "autoFocus":True},
      "chipLayout":{"size":"small"},
      "expand": False,
      "heroData": [
          {
              "index": 0,
              "name": "Beatrix",
              "img": "https://static.expertwm.com/mlbb/heroes/beatrix.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 1,
              "name": "Brody",
              "img": "https://static.expertwm.com/mlbb/heroes/brody.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 2,
              "name": "Bruno",
              "img": "https://static.expertwm.com/mlbb/heroes/bruno.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 3,
              "name": "Claude",
              "img": "https://static.expertwm.com/mlbb/heroes/claude.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 4,
              "name": "Clint",
              "img": "https://static.expertwm.com/mlbb/heroes/clint.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 5,
              "name": "Granger",
              "img": "https://static.expertwm.com/mlbb/heroes/granger.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
  
            {
              "index": 6,
              "name": "Beatrix",
              "img": "https://static.expertwm.com/mlbb/heroes/beatrix.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 7,
              "name": "Brody",
              "img": "https://static.expertwm.com/mlbb/heroes/brody.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 8,
              "name": "Bruno",
              "img": "https://static.expertwm.com/mlbb/heroes/bruno.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 9,
              "name": "Claude",
              "img": "https://static.expertwm.com/mlbb/heroes/claude.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 10,
              "name": "Clint",
              "img": "https://static.expertwm.com/mlbb/heroes/clint.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 11,
              "name": "Granger",
              "img": "https://static.expertwm.com/mlbb/heroes/granger.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
      ],
      "equipmentList": [
        {
          "index": 0,
          "name": "Tough Boots",
          "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
        },
        {
          "index": 1,
          "name": "Tough Boots",
          "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
        },
        {
          "index": 2,
          "name": "Tough Boots",
          "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
        },
        {
          "index": 3,
          "name": "Tough Boots",
          "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
        },
        {
          "index": 4,
          "name": "Tough Boots",
          "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
        },
        {
          "index": 5,
          "name": "Tough Boots",
          "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
        }
      ],
      "equipmentCategory": [
        { "index": 0, "name": "Attack", "color": "#880808" },
        { "index": 1, "name": "Magic", "color": "#0047AB" },
        { "index": 2, "name": "Defense", "color": "#50C878" }
        # { "index": 3, "name": "Movement", "color": "#C19A6B" },
        # { "index": 4, "name": "Jungling", "color": "#702963" },
        # { "index": 5, "name": "Roaming", "color": "#40B5AD" }
      ],
      "top3Equipment": [
        { "index": 0, "name": "Health", "stat": "+4453" },
        { "index": 1, "name": "Magic Power", "stat": "+589" },
        { "index": 2, "name": "Atk Speed", "stat": "+33%" }
      ],
      "bottom3Equipment": [
        { "index": 0, "name": "Health", "stat": "+4453" },
        { "index": 1, "name": "Magic Power", "stat": "+589" },
        { "index": 2, "name": "Atk Speed", "stat": "+33%" }
      ],
      "expandData": [
        {
          "index": 0,
          "tabTitle": "Visualize",
          "toggle": False,
          "vizualizeD": [
            {
              "index": 0,
              "equipCatChecked": False,
              "dataToDisplayOriginal": [
                {
                  "skillFeature": "Attack_Speed",
                  "total": 190,
                  "attack": 20,
                  "magic": 30,
                  "defense": 30,
                  "movement": 70,
                  "jungling": 15,
                  "roaming": 15
                },
                {
                  "skillFeature": "CD_Reduction",
                  "total": 100,
                  "attack": 20,
                  "magic": 30,
                  "defense": 10,
                  "movement": 10,
                  "jungling": 15,
                  "roaming": 15
                },
                {
                  "skillFeature": "Crit_Chance",
                  "total": 50,
                  "attack": 20,
                  "magic": 5,
                  "defense": 5,
                  "movement": 5,
                  "jungling": 5,
                  "roaming": 10
                }
              ],
              "keysOrigin": [
                "total",
                "attack",
                "magic",
                "defense",
                "movement",
                "jungling",
                "roaming"
              ],
              "dataToDisplayCat": [
                {
                  "skillFeature": "Attack_Speed",
                  "total": 190,
                  "attack": 20,
                  "magic": 30,
                  "defense": 30,
                  "movement": 70,
                  "jungling": 15,
                  "roaming": 15
                },
                {
                  "skillFeature": "CD_Reduction",
                  "total": 100,
                  "attack": 20,
                  "magic": 30,
                  "defense": 10,
                  "movement": 10,
                  "jungling": 15,
                  "roaming": 15
                },
                {
                  "skillFeature": "Crit_Chance",
                  "total": 50,
                  "attack": 20,
                  "magic": 5,
                  "defense": 5,
                  "movement": 5,
                  "jungling": 5,
                  "roaming": 10
                }
              ],
              "chartLayout": {
                "keys": ["total"],
                "indexBy": "skillFeature",
                "margin": { "right": 85, "bottom": 40, "left": 30, "top": 20 },
                "labelSkipHeight": 12,
                "legends": [
                  {
                    "dataFrom": "keys",
                    "anchor": "bottom-right",
                    "direction": "column",
                    "justify": False,
                    "translateX": 100,
                    "translateY": 0,
                    "itemsSpacing": 2,
                    "itemWidth": 100,
                    "itemHeight": 20,
                    "itemDirection": "left-to-right",
                    "itemOpacity": 0.85,
                    "symbolSize": 20,
                    "effects": [
                      {
                        "on": "hover",
                        "style": {
                          "itemOpacity": 1
                        }
                      }
                    ]
                  }
                ]
              }
            }
          ],
          "gridD": [
            { "index": 0, "name": "Attack_Speed", "stat": "34%" },
            { "index": 1, "name": "CD_Reduction", "stat": "8%" },
            { "index": 2, "name": "Crit_Chance", "stat": "14%" },
            { "index": 3, "name": "HP", "stat": "4560" },
            { "index": 4, "name": "HP_Regen", "stat": "8" },
            { "index": 5, "name": "Hybrid_Lifesteal", "stat": "8" },
            { "index": 6, "name": "Lifesteal", "stat": "12" },
            { "index": 7, "name": "Magic_Defense", "stat": "115" },
            { "index": 8, "name": "Magic_Lifesteal", "stat": "7" },
            { "index": 9, "name": "Magic_PEN", "stat": "25%" },
            { "index": 10, "name": "Magic_Power", "stat": "308" },
            { "index": 11, "name": "Mana", "stat": "100" },
            { "index": 12, "name": "Mana_Regen", "stat": "8" },
            { "index": 13, "name": "Movement_Speed", "stat": "70" },
            { "index": 14, "name": "Physical_Attack", "stat": "689" },
            { "index": 15, "name": "Physical_Defense", "stat": "350" },
            { "index": 16, "name": "Spell_Vamp", "stat": "8" }
          ]
        }
      ]
    },
        {
        "index": 1,
        "addNewHero":False,
        "toStore":False,
         "hasChanged":False,
        "remove":False,
      "confirmRemove":False, 
      "clickedChange":False,
      "ratings":0,
      "numOfUsersRatedVal": 80,
        "indexName": "equipmentItems",
        "title": "Jake is here",
        "titleVal":"equipment name",
        "numOfHeroes": [
            {
            "index": 0,
            "sum": "+7",
            "expand": True,
            "heroesUserAttachedToSet": [ ]
            }
        ],
        "changeTitleBtnLayout":{"disabled":True},
        "changeTitleTxtF":{"value":"", "autoFocus":True},
        "chipLayout":{"size":"small"},
        "expand": False,
        "heroData": [
            {
                "index": 0,
                "name": "Beatrix",
                "img": "https://static.expertwm.com/mlbb/heroes/beatrix.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 1,
                "name": "Brody",
                "img": "https://static.expertwm.com/mlbb/heroes/brody.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 2,
                "name": "Bruno",
                "img": "https://static.expertwm.com/mlbb/heroes/bruno.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 3,
                "name": "Claude",
                "img": "https://static.expertwm.com/mlbb/heroes/claude.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 4,
                "name": "Clint",
                "img": "https://static.expertwm.com/mlbb/heroes/clint.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 5,
                "name": "Granger",
                "img": "https://static.expertwm.com/mlbb/heroes/granger.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
    
                {
                "index": 6,
                "name": "Beatrix",
                "img": "https://static.expertwm.com/mlbb/heroes/beatrix.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 7,
                "name": "Brody",
                "img": "https://static.expertwm.com/mlbb/heroes/brody.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 8,
                "name": "Bruno",
                "img": "https://static.expertwm.com/mlbb/heroes/bruno.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 9,
                "name": "Claude",
                "img": "https://static.expertwm.com/mlbb/heroes/claude.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 10,
                "name": "Clint",
                "img": "https://static.expertwm.com/mlbb/heroes/clint.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 11,
                "name": "Granger",
                "img": "https://static.expertwm.com/mlbb/heroes/granger.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
        ],
        "equipmentList": [
            {
            "index": 0,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            },
            {
            "index": 1,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            },
            {
            "index": 2,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            },
            {
            "index": 3,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            },
            {
            "index": 4,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            },
            {
            "index": 5,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            }
        ],
        "equipmentCategory": [
            { "index": 0, "name": "Attack", "color": "#880808" },
            { "index": 1, "name": "Magic", "color": "#0047AB" },
            { "index": 2, "name": "Defense", "color": "#50C878" }
            # { "index": 3, "name": "Movement", "color": "#C19A6B" },
            # { "index": 4, "name": "Jungling", "color": "#702963" },
            # { "index": 5, "name": "Roaming", "color": "#40B5AD" }
        ],
        "top3Equipment": [
            { "index": 0, "name": "Health", "stat": "+4453" },
            { "index": 1, "name": "Magic Power", "stat": "+589" },
            { "index": 2, "name": "Atk Speed", "stat": "+33%" }
        ],
        "bottom3Equipment": [
            { "index": 0, "name": "Health", "stat": "+4453" },
            { "index": 1, "name": "Magic Power", "stat": "+589" },
            { "index": 2, "name": "Atk Speed", "stat": "+33%" }
        ],
        "expandData": [
            {
            "index": 0,
            "tabTitle": "Visualize",
            "toggle": False,
            "vizualizeD": [
                {
                "index": 0,
                "equipCatChecked": False,
                "dataToDisplayOriginal": [
                    {
                    "skillFeature": "Attack_Speed",
                    "total": 190,
                    "attack": 20,
                    "magic": 30,
                    "defense": 30,
                    "movement": 70,
                    "jungling": 15,
                    "roaming": 15
                    },
                    {
                    "skillFeature": "CD_Reduction",
                    "total": 100,
                    "attack": 20,
                    "magic": 30,
                    "defense": 10,
                    "movement": 10,
                    "jungling": 15,
                    "roaming": 15
                    },
                    {
                    "skillFeature": "Crit_Chance",
                    "total": 50,
                    "attack": 20,
                    "magic": 5,
                    "defense": 5,
                    "movement": 5,
                    "jungling": 5,
                    "roaming": 10
                    }
                ],
                "keysOrigin": [
                    "total",
                    "attack",
                    "magic",
                    "defense",
                    "movement",
                    "jungling",
                    "roaming"
                ],
                "dataToDisplayCat": [
                    {
                    "skillFeature": "Attack_Speed",
                    "total": 190,
                    "attack": 20,
                    "magic": 30,
                    "defense": 30,
                    "movement": 70,
                    "jungling": 15,
                    "roaming": 15
                    },
                    {
                    "skillFeature": "CD_Reduction",
                    "total": 100,
                    "attack": 20,
                    "magic": 30,
                    "defense": 10,
                    "movement": 10,
                    "jungling": 15,
                    "roaming": 15
                    },
                    {
                    "skillFeature": "Crit_Chance",
                    "total": 50,
                    "attack": 20,
                    "magic": 5,
                    "defense": 5,
                    "movement": 5,
                    "jungling": 5,
                    "roaming": 10
                    }
                ],
                "chartLayout": {
                    "keys": ["total"],
                    "indexBy": "skillFeature",
                    "margin": { "right": 85, "bottom": 40, "left": 30, "top": 20 },
                    "labelSkipHeight": 12,
                    "legends": [
                    {
                        "dataFrom": "keys",
                        "anchor": "bottom-right",
                        "direction": "column",
                        "justify": False,
                        "translateX": 100,
                        "translateY": 0,
                        "itemsSpacing": 2,
                        "itemWidth": 100,
                        "itemHeight": 20,
                        "itemDirection": "left-to-right",
                        "itemOpacity": 0.85,
                        "symbolSize": 20,
                        "effects": [
                        {
                            "on": "hover",
                            "style": {
                            "itemOpacity": 1
                            }
                        }
                        ]
                    }
                    ]
                }
                }
            ],
            "gridD": [
                { "index": 0, "name": "Attack_Speed", "stat": "34%" },
                { "index": 1, "name": "CD_Reduction", "stat": "8%" },
                { "index": 2, "name": "Crit_Chance", "stat": "14%" },
                { "index": 3, "name": "HP", "stat": "4560" },
                { "index": 4, "name": "HP_Regen", "stat": "8" },
                { "index": 5, "name": "Hybrid_Lifesteal", "stat": "8" },
                { "index": 6, "name": "Lifesteal", "stat": "12" },
                { "index": 7, "name": "Magic_Defense", "stat": "115" },
                { "index": 8, "name": "Magic_Lifesteal", "stat": "7" },
                { "index": 9, "name": "Magic_PEN", "stat": "25%" },
                { "index": 10, "name": "Magic_Power", "stat": "308" },
                { "index": 11, "name": "Mana", "stat": "100" },
                { "index": 12, "name": "Mana_Regen", "stat": "8" },
                { "index": 13, "name": "Movement_Speed", "stat": "70" },
                { "index": 14, "name": "Physical_Attack", "stat": "689" },
                { "index": 15, "name": "Physical_Defense", "stat": "350" },
                { "index": 16, "name": "Spell_Vamp", "stat": "8" }
            ]
            }
        ]
        },
        {
        "index": 2,
        "addNewHero":False,
        "toStore":False,
         "hasChanged":False,
        "remove":False,
      "confirmRemove":False,
      "clickedChange":False,
        "ratings":0,
        "numOfUsersRatedVal": 80,
        "indexName": "equipmentItems",
        "title": "Equipment name",
        "titleVal":"equipment name",
        "numOfHeroes": [
            {
            "index": 0,
            "sum": "+7",
            "expand": True,
            "heroesUserAttachedToSet": [ ]
            }
        ],
        "changeTitleBtnLayout":{"disabled":True},
        "changeTitleTxtF":{"value":"", "autoFocus":True},
        "chipLayout":{"size":"small"},
        "expand": False,
        "heroData": [
            {
                "index": 0,
                "name": "Beatrix",
                "img": "https://static.expertwm.com/mlbb/heroes/beatrix.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 1,
                "name": "Brody",
                "img": "https://static.expertwm.com/mlbb/heroes/brody.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 2,
                "name": "Bruno",
                "img": "https://static.expertwm.com/mlbb/heroes/bruno.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 3,
                "name": "Claude",
                "img": "https://static.expertwm.com/mlbb/heroes/claude.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 4,
                "name": "Clint",
                "img": "https://static.expertwm.com/mlbb/heroes/clint.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 5,
                "name": "Granger",
                "img": "https://static.expertwm.com/mlbb/heroes/granger.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
    
                {
                "index": 6,
                "name": "Beatrix",
                "img": "https://static.expertwm.com/mlbb/heroes/beatrix.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 7,
                "name": "Brody",
                "img": "https://static.expertwm.com/mlbb/heroes/brody.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 8,
                "name": "Bruno",
                "img": "https://static.expertwm.com/mlbb/heroes/bruno.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 9,
                "name": "Claude",
                "img": "https://static.expertwm.com/mlbb/heroes/claude.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 10,
                "name": "Clint",
                "img": "https://static.expertwm.com/mlbb/heroes/clint.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 11,
                "name": "Granger",
                "img": "https://static.expertwm.com/mlbb/heroes/granger.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
        ],
        "equipmentList": [
            {
            "index": 0,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            },
            {
            "index": 1,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            },
            {
            "index": 2,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            },
            {
            "index": 3,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            },
            {
            "index": 4,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            },
            {
            "index": 5,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            }
        ],
        "equipmentCategory": [
            { "index": 0, "name": "Attack", "color": "#880808" },
            { "index": 1, "name": "Magic", "color": "#0047AB" },
            { "index": 2, "name": "Defense", "color": "#50C878" }
            # { "index": 3, "name": "Movement", "color": "#C19A6B" },
            # { "index": 4, "name": "Jungling", "color": "#702963" },
            # { "index": 5, "name": "Roaming", "color": "#40B5AD" }
        ],
        "top3Equipment": [
            { "index": 0, "name": "Health", "stat": "+4453" },
            { "index": 1, "name": "Magic Power", "stat": "+589" },
            { "index": 2, "name": "Atk Speed", "stat": "+33%" }
        ],
        "bottom3Equipment": [
            { "index": 0, "name": "Health", "stat": "+4453" },
            { "index": 1, "name": "Magic Power", "stat": "+589" },
            { "index": 2, "name": "Atk Speed", "stat": "+33%" }
        ],
        "expandData": [
            {
            "index": 0,
            "tabTitle": "Visualize",
            "toggle": False,
            "vizualizeD": [
                {
                "index": 0,
                "equipCatChecked": False,
                "dataToDisplayOriginal": [
                    {
                    "skillFeature": "Attack_Speed",
                    "total": 190,
                    "attack": 20,
                    "magic": 30,
                    "defense": 30,
                    "movement": 70,
                    "jungling": 15,
                    "roaming": 15
                    },
                    {
                    "skillFeature": "CD_Reduction",
                    "total": 100,
                    "attack": 20,
                    "magic": 30,
                    "defense": 10,
                    "movement": 10,
                    "jungling": 15,
                    "roaming": 15
                    },
                    {
                    "skillFeature": "Crit_Chance",
                    "total": 50,
                    "attack": 20,
                    "magic": 5,
                    "defense": 5,
                    "movement": 5,
                    "jungling": 5,
                    "roaming": 10
                    }
                ],
                "keysOrigin": [
                    "total",
                    "attack",
                    "magic",
                    "defense",
                    "movement",
                    "jungling",
                    "roaming"
                ],
                "dataToDisplayCat": [
                    {
                    "skillFeature": "Attack_Speed",
                    "total": 190,
                    "attack": 20,
                    "magic": 30,
                    "defense": 30,
                    "movement": 70,
                    "jungling": 15,
                    "roaming": 15
                    },
                    {
                    "skillFeature": "CD_Reduction",
                    "total": 100,
                    "attack": 20,
                    "magic": 30,
                    "defense": 10,
                    "movement": 10,
                    "jungling": 15,
                    "roaming": 15
                    },
                    {
                    "skillFeature": "Crit_Chance",
                    "total": 50,
                    "attack": 20,
                    "magic": 5,
                    "defense": 5,
                    "movement": 5,
                    "jungling": 5,
                    "roaming": 10
                    }
                ],
                "chartLayout": {
                    "keys": ["total"],
                    "indexBy": "skillFeature",
                    "margin": { "right": 85, "bottom": 40, "left": 30, "top": 20 },
                    "labelSkipHeight": 12,
                    "legends": [
                    {
                        "dataFrom": "keys",
                        "anchor": "bottom-right",
                        "direction": "column",
                        "justify": False,
                        "translateX": 100,
                        "translateY": 0,
                        "itemsSpacing": 2,
                        "itemWidth": 100,
                        "itemHeight": 20,
                        "itemDirection": "left-to-right",
                        "itemOpacity": 0.85,
                        "symbolSize": 20,
                        "effects": [
                        {
                            "on": "hover",
                            "style": {
                            "itemOpacity": 1
                            }
                        }
                        ]
                    }
                    ]
                }
                }
            ],
            "gridD": [
                { "index": 0, "name": "Attack_Speed", "stat": "34%" },
                { "index": 1, "name": "CD_Reduction", "stat": "8%" },
                { "index": 2, "name": "Crit_Chance", "stat": "14%" },
                { "index": 3, "name": "HP", "stat": "4560" },
                { "index": 4, "name": "HP_Regen", "stat": "8" },
                { "index": 5, "name": "Hybrid_Lifesteal", "stat": "8" },
                { "index": 6, "name": "Lifesteal", "stat": "12" },
                { "index": 7, "name": "Magic_Defense", "stat": "115" },
                { "index": 8, "name": "Magic_Lifesteal", "stat": "7" },
                { "index": 9, "name": "Magic_PEN", "stat": "25%" },
                { "index": 10, "name": "Magic_Power", "stat": "308" },
                { "index": 11, "name": "Mana", "stat": "100" },
                { "index": 12, "name": "Mana_Regen", "stat": "8" },
                { "index": 13, "name": "Movement_Speed", "stat": "70" },
                { "index": 14, "name": "Physical_Attack", "stat": "689" },
                { "index": 15, "name": "Physical_Defense", "stat": "350" },
                { "index": 16, "name": "Spell_Vamp", "stat": "8" }
            ]
            }
        ]
        },
        {
        "index": 3,
        "addNewHero":False,
        "toStore":False,
         "hasChanged":False,
        "remove":False,
      "confirmRemove":False,
      "clickedChange":False,
        "ratings":0,
        "numOfUsersRatedVal": 80,
        "indexName": "equipmentItems",
        "title": "Equipment name",
        "numOfHeroes": [
            {
            "index": 0,
            "sum": "+7",
            "expand": True,
            "heroesUserAttachedToSet": [ ]
            }
        ],
        "changeTitleBtnLayout":{"disabled":True},
        "changeTitleTxtF":{"value":"", "autoFocus":True},
        "chipLayout":{"size":"small"},
        "expand": False,
        "heroData": [
            {
                "index": 0,
                "name": "Beatrix",
                "img": "https://static.expertwm.com/mlbb/heroes/beatrix.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 1,
                "name": "Brody",
                "img": "https://static.expertwm.com/mlbb/heroes/brody.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 2,
                "name": "Bruno",
                "img": "https://static.expertwm.com/mlbb/heroes/bruno.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 3,
                "name": "Claude",
                "img": "https://static.expertwm.com/mlbb/heroes/claude.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 4,
                "name": "Clint",
                "img": "https://static.expertwm.com/mlbb/heroes/clint.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 5,
                "name": "Granger",
                "img": "https://static.expertwm.com/mlbb/heroes/granger.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
    
                {
                "index": 6,
                "name": "Beatrix",
                "img": "https://static.expertwm.com/mlbb/heroes/beatrix.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 7,
                "name": "Brody",
                "img": "https://static.expertwm.com/mlbb/heroes/brody.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 8,
                "name": "Bruno",
                "img": "https://static.expertwm.com/mlbb/heroes/bruno.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 9,
                "name": "Claude",
                "img": "https://static.expertwm.com/mlbb/heroes/claude.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 10,
                "name": "Clint",
                "img": "https://static.expertwm.com/mlbb/heroes/clint.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
                {
                "index": 11,
                "name": "Granger",
                "img": "https://static.expertwm.com/mlbb/heroes/granger.png?w=64",
                "clicked":False, "Layout":{"color":"default"}
                },
        ],
        "equipmentList": [
            {
            "index": 0,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            },
            {
            "index": 1,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            },
            {
            "index": 2,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            },
            {
            "index": 3,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            },
            {
            "index": 4,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            },
            {
            "index": 5,
            "name": "Tough Boots",
            "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
            }
        ],
        "equipmentCategory": [
            { "index": 0, "name": "Attack", "color": "#880808" },
            { "index": 1, "name": "Magic", "color": "#0047AB" },
            { "index": 2, "name": "Defense", "color": "#50C878" }
            # { "index": 3, "name": "Movement", "color": "#C19A6B" },
            # { "index": 4, "name": "Jungling", "color": "#702963" },
            # { "index": 5, "name": "Roaming", "color": "#40B5AD" }
        ],
        "top3Equipment": [
            { "index": 0, "name": "Health", "stat": "+4453" },
            { "index": 1, "name": "Magic Power", "stat": "+589" },
            { "index": 2, "name": "Atk Speed", "stat": "+33%" }
        ],
        "bottom3Equipment": [
            { "index": 0, "name": "Health", "stat": "+4453" },
            { "index": 1, "name": "Magic Power", "stat": "+589" },
            { "index": 2, "name": "Atk Speed", "stat": "+33%" }
        ],
        "expandData": [
            {
            "index": 0,
            "tabTitle": "Visualize",
            "toggle": False,
            "vizualizeD": [
                {
                "index": 0,
                "equipCatChecked": False,
                "dataToDisplayOriginal": [
                    {
                    "skillFeature": "Attack_Speed",
                    "total": 190,
                    "attack": 20,
                    "magic": 30,
                    "defense": 30,
                    "movement": 70,
                    "jungling": 15,
                    "roaming": 15
                    },
                    {
                    "skillFeature": "CD_Reduction",
                    "total": 100,
                    "attack": 20,
                    "magic": 30,
                    "defense": 10,
                    "movement": 10,
                    "jungling": 15,
                    "roaming": 15
                    },
                    {
                    "skillFeature": "Crit_Chance",
                    "total": 50,
                    "attack": 20,
                    "magic": 5,
                    "defense": 5,
                    "movement": 5,
                    "jungling": 5,
                    "roaming": 10
                    }
                ],
                "keysOrigin": [
                    "total",
                    "attack",
                    "magic",
                    "defense",
                    "movement",
                    "jungling",
                    "roaming"
                ],
                "dataToDisplayCat": [
                    {
                    "skillFeature": "Attack_Speed",
                    "total": 190,
                    "attack": 20,
                    "magic": 30,
                    "defense": 30,
                    "movement": 70,
                    "jungling": 15,
                    "roaming": 15
                    },
                    {
                    "skillFeature": "CD_Reduction",
                    "total": 100,
                    "attack": 20,
                    "magic": 30,
                    "defense": 10,
                    "movement": 10,
                    "jungling": 15,
                    "roaming": 15
                    },
                    {
                    "skillFeature": "Crit_Chance",
                    "total": 50,
                    "attack": 20,
                    "magic": 5,
                    "defense": 5,
                    "movement": 5,
                    "jungling": 5,
                    "roaming": 10
                    }
                ],
                "chartLayout": {
                    "keys": ["total"],
                    "indexBy": "skillFeature",
                    "margin": { "right": 85, "bottom": 40, "left": 30, "top": 20 },
                    "labelSkipHeight": 12,
                    "legends": [
                    {
                        "dataFrom": "keys",
                        "anchor": "bottom-right",
                        "direction": "column",
                        "justify": False,
                        "translateX": 100,
                        "translateY": 0,
                        "itemsSpacing": 2,
                        "itemWidth": 100,
                        "itemHeight": 20,
                        "itemDirection": "left-to-right",
                        "itemOpacity": 0.85,
                        "symbolSize": 20,
                        "effects": [
                        {
                            "on": "hover",
                            "style": {
                            "itemOpacity": 1
                            }
                        }
                        ]
                    }
                    ]
                }
                }
            ],
            "gridD": [
                { "index": 0, "name": "Attack_Speed", "stat": "34%" },
                { "index": 1, "name": "CD_Reduction", "stat": "8%" },
                { "index": 2, "name": "Crit_Chance", "stat": "14%" },
                { "index": 3, "name": "HP", "stat": "4560" },
                { "index": 4, "name": "HP_Regen", "stat": "8" },
                { "index": 5, "name": "Hybrid_Lifesteal", "stat": "8" },
                { "index": 6, "name": "Lifesteal", "stat": "12" },
                { "index": 7, "name": "Magic_Defense", "stat": "115" },
                { "index": 8, "name": "Magic_Lifesteal", "stat": "7" },
                { "index": 9, "name": "Magic_PEN", "stat": "25%" },
                { "index": 10, "name": "Magic_Power", "stat": "308" },
                { "index": 11, "name": "Mana", "stat": "100" },
                { "index": 12, "name": "Mana_Regen", "stat": "8" },
                { "index": 13, "name": "Movement_Speed", "stat": "70" },
                { "index": 14, "name": "Physical_Attack", "stat": "689" },
                { "index": 15, "name": "Physical_Defense", "stat": "350" },
                { "index": 16, "name": "Spell_Vamp", "stat": "8" }
            ]
            }
        ]
        },
        {
      "index": 4,
      "addNewHero":False,
      "toStore":False,
       "hasChanged":False,
      "remove":False,
      "confirmRemove":False,
      "clickedChange":False,
     "ratings":0,
     "numOfUsersRatedVal": 80,
      "indexName": "equipmentItems",
      "title": "Equipment name",
      "titleVal":"equipment name",
      "numOfHeroes": [
        {
          "index": 0,
          "sum": "+7",
          "expand": True,
         "heroesUserAttachedToSet": [ ]
        }
      ],
      "changeTitleBtnLayout":{"disabled":True},
      "changeTitleTxtF":{"value":"", "autoFocus":True},
      "chipLayout":{"size":"small"},
      "expand": False,
      "heroData": [
          {
              "index": 0,
              "name": "Beatrix",
              "img": "https://static.expertwm.com/mlbb/heroes/beatrix.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 1,
              "name": "Brody",
              "img": "https://static.expertwm.com/mlbb/heroes/brody.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 2,
              "name": "Bruno",
              "img": "https://static.expertwm.com/mlbb/heroes/bruno.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 3,
              "name": "Claude",
              "img": "https://static.expertwm.com/mlbb/heroes/claude.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 4,
              "name": "Clint",
              "img": "https://static.expertwm.com/mlbb/heroes/clint.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 5,
              "name": "Granger",
              "img": "https://static.expertwm.com/mlbb/heroes/granger.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
  
            {
              "index": 6,
              "name": "Beatrix",
              "img": "https://static.expertwm.com/mlbb/heroes/beatrix.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 7,
              "name": "Brody",
              "img": "https://static.expertwm.com/mlbb/heroes/brody.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 8,
              "name": "Bruno",
              "img": "https://static.expertwm.com/mlbb/heroes/bruno.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 9,
              "name": "Claude",
              "img": "https://static.expertwm.com/mlbb/heroes/claude.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 10,
              "name": "Clint",
              "img": "https://static.expertwm.com/mlbb/heroes/clint.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
            {
              "index": 11,
              "name": "Granger",
              "img": "https://static.expertwm.com/mlbb/heroes/granger.png?w=64",
               "clicked":False, "Layout":{"color":"default"}
            },
      ],
      "equipmentList": [
        {
          "index": 0,
          "name": "Tough Boots",
          "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
        },
        {
          "index": 1,
          "name": "Tough Boots",
          "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
        },
        {
          "index": 2,
          "name": "Tough Boots",
          "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
        },
        {
          "index": 3,
          "name": "Tough Boots",
          "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
        },
        {
          "index": 4,
          "name": "Tough Boots",
          "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
        },
        {
          "index": 5,
          "name": "Tough Boots",
          "img": "https://static.expertwm.com/mlbb/items/tough-boots.png"
        }
      ],
      "equipmentCategory": [
        { "index": 0, "name": "Attack", "color": "#880808" },
        { "index": 1, "name": "Magic", "color": "#0047AB" },
        { "index": 2, "name": "Defense", "color": "#50C878" }
        # { "index": 3, "name": "Movement", "color": "#C19A6B" },
        # { "index": 4, "name": "Jungling", "color": "#702963" },
        # { "index": 5, "name": "Roaming", "color": "#40B5AD" }
      ],
      "top3Equipment": [
        { "index": 0, "name": "Health", "stat": "+4453" },
        { "index": 1, "name": "Magic Power", "stat": "+589" },
        { "index": 2, "name": "Atk Speed", "stat": "+33%" }
      ],
      "bottom3Equipment": [
        { "index": 0, "name": "Health", "stat": "+4453" },
        { "index": 1, "name": "Magic Power", "stat": "+589" },
        { "index": 2, "name": "Atk Speed", "stat": "+33%" }
      ],
      "expandData": [
        {
          "index": 0,
          "tabTitle": "Visualize",
          "toggle": False,
          "vizualizeD": [
            {
              "index": 0,
              "equipCatChecked": False,
              "dataToDisplayOriginal": [
                {
                  "skillFeature": "Attack_Speed",
                  "total": 190,
                  "attack": 20,
                  "magic": 30,
                  "defense": 30,
                  "movement": 70,
                  "jungling": 15,
                  "roaming": 15
                },
                {
                  "skillFeature": "CD_Reduction",
                  "total": 100,
                  "attack": 20,
                  "magic": 30,
                  "defense": 10,
                  "movement": 10,
                  "jungling": 15,
                  "roaming": 15
                },
                {
                  "skillFeature": "Crit_Chance",
                  "total": 50,
                  "attack": 20,
                  "magic": 5,
                  "defense": 5,
                  "movement": 5,
                  "jungling": 5,
                  "roaming": 10
                }
              ],
              "keysOrigin": [
                "total",
                "attack",
                "magic",
                "defense",
                "movement",
                "jungling",
                "roaming"
              ],
              "dataToDisplayCat": [
                {
                  "skillFeature": "Attack_Speed",
                  "total": 190,
                  "attack": 20,
                  "magic": 30,
                  "defense": 30,
                  "movement": 70,
                  "jungling": 15,
                  "roaming": 15
                },
                {
                  "skillFeature": "CD_Reduction",
                  "total": 100,
                  "attack": 20,
                  "magic": 30,
                  "defense": 10,
                  "movement": 10,
                  "jungling": 15,
                  "roaming": 15
                },
                {
                  "skillFeature": "Crit_Chance",
                  "total": 50,
                  "attack": 20,
                  "magic": 5,
                  "defense": 5,
                  "movement": 5,
                  "jungling": 5,
                  "roaming": 10
                }
              ],
              "chartLayout": {
                "keys": ["total"],
                "indexBy": "skillFeature",
                "margin": { "right": 85, "bottom": 40, "left": 30, "top": 20 },
                "labelSkipHeight": 12,
                "legends": [
                  {
                    "dataFrom": "keys",
                    "anchor": "bottom-right",
                    "direction": "column",
                    "justify": False,
                    "translateX": 100,
                    "translateY": 0,
                    "itemsSpacing": 2,
                    "itemWidth": 100,
                    "itemHeight": 20,
                    "itemDirection": "left-to-right",
                    "itemOpacity": 0.85,
                    "symbolSize": 20,
                    "effects": [
                      {
                        "on": "hover",
                        "style": {
                          "itemOpacity": 1
                        }
                      }
                    ]
                  }
                ]
              }
            }
          ],
          "gridD": [
            { "index": 0, "name": "Attack_Speed", "stat": "34%" },
            { "index": 1, "name": "CD_Reduction", "stat": "8%" },
            { "index": 2, "name": "Crit_Chance", "stat": "14%" },
            { "index": 3, "name": "HP", "stat": "4560" },
            { "index": 4, "name": "HP_Regen", "stat": "8" },
            { "index": 5, "name": "Hybrid_Lifesteal", "stat": "8" },
            { "index": 6, "name": "Lifesteal", "stat": "12" },
            { "index": 7, "name": "Magic_Defense", "stat": "115" },
            { "index": 8, "name": "Magic_Lifesteal", "stat": "7" },
            { "index": 9, "name": "Magic_PEN", "stat": "25%" },
            { "index": 10, "name": "Magic_Power", "stat": "308" },
            { "index": 11, "name": "Mana", "stat": "100" },
            { "index": 12, "name": "Mana_Regen", "stat": "8" },
            { "index": 13, "name": "Movement_Speed", "stat": "70" },
            { "index": 14, "name": "Physical_Attack", "stat": "689" },
            { "index": 15, "name": "Physical_Defense", "stat": "350" },
            { "index": 16, "name": "Spell_Vamp", "stat": "8" }
          ]
        }
      ]
    },
     
    ]

    data = [
  {
    "confirmRemove": False,
    "changeTitleTxtF": {
      "value": "Mike"
    },
    "indexName": "equipmentItems",
    "index": 0,
    "heroData": [
      {
        "img": "https://static.expertwm.com/mlbb/heroes/miya.png?w=64",
        "index": 0,
        "Layout": {
          "color": "primary"
        },
        "clicked": True,
        "name": "Miya"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/balmond.png?w=64",
        "index": 1,
        "Layout": {
          "color": "primary"
        },
        "clicked": True,
        "name": "Balmond"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/saber.png?w=64",
        "index": 2,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Saber"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/alice.png?w=64",
        "index": 3,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Alice"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/nana.png?w=64",
        "index": 4,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Nana"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/tigreal.png?w=64",
        "index": 5,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Tigreal"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/alucard.png?w=64",
        "index": 6,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Alucard"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/karina.png?w=64",
        "index": 7,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Karina"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/akai.png?w=64",
        "index": 8,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Akai"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/franco.png?w=64",
        "index": 9,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Franco"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/bane.png?w=64",
        "index": 10,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Bane"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/bruno.png?w=64",
        "index": 11,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Bruno"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/clint.png?w=64",
        "index": 12,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Clint"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/rafaela.png?w=64",
        "index": 13,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Rafaela"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/eudora.png?w=64",
        "index": 14,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Eudora"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/zilong.png?w=64",
        "index": 15,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Zilong"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/fanny.png?w=64",
        "index": 16,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Fanny"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/layla.png?w=64",
        "index": 17,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Layla"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/minotaur.png?w=64",
        "index": 18,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Minotaur"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/lolita.png?w=64",
        "index": 19,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Lolita"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/hayabusa.png?w=64",
        "index": 20,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Hayabusa"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/freya.png?w=64",
        "index": 21,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Freya"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/gord.png?w=64",
        "index": 22,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Gord"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/natalia.png?w=64",
        "index": 23,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Natalia"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/kagura.png?w=64",
        "index": 24,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Kagura"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/chou.png?w=64",
        "index": 25,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Chou"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/sun.png?w=64",
        "index": 26,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Sun"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/alpha.png?w=64",
        "index": 27,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Alpha"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/ruby.png?w=64",
        "index": 28,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Ruby"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/yi-sun-shin.png?w=64",
        "index": 29,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Yi Sun-shin"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/moskov.png?w=64",
        "index": 30,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Moskov"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/johnson.png?w=64",
        "index": 31,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Johnson"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/cyclops.png?w=64",
        "index": 32,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Cyclops"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/estes.png?w=64",
        "index": 33,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Estes"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/hilda.png?w=64",
        "index": 34,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Hilda"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/aurora.png?w=64",
        "index": 35,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Aurora"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/lapu-lapu.png?w=64",
        "index": 36,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Lapu-Lapu"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/vexana.png?w=64",
        "index": 37,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Vexana"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/roger.png?w=64",
        "index": 38,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Roger"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/karrie.png?w=64",
        "index": 39,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Karrie"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/gatotkaca.png?w=64",
        "index": 40,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Gatotkaca"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/harley.png?w=64",
        "index": 41,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Harley"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/irithel.png?w=64",
        "index": 42,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Irithel"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/grock.png?w=64",
        "index": 43,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Grock"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/argus.png?w=64",
        "index": 44,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Argus"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/odette.png?w=64",
        "index": 45,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Odette"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/lancelot.png?w=64",
        "index": 46,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Lancelot"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/diggie.png?w=64",
        "index": 47,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Diggie"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/hylos.png?w=64",
        "index": 48,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Hylos"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/zhask.png?w=64",
        "index": 49,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Zhask"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/helcurt.png?w=64",
        "index": 50,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Helcurt"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/pharsa.png?w=64",
        "index": 51,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Pharsa"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/lesley.png?w=64",
        "index": 52,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Lesley"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/jawhead.png?w=64",
        "index": 53,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Jawhead"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/angela.png?w=64",
        "index": 54,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Angela"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/gusion.png?w=64",
        "index": 55,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Gusion"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/valir.png?w=64",
        "index": 56,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Valir"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/martis.png?w=64",
        "index": 57,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Martis"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/uranus.png?w=64",
        "index": 58,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Uranus"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/hanabi.png?w=64",
        "index": 59,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Hanabi"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/chang-e.png?w=64",
        "index": 60,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Chang'e"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/kaja.png?w=64",
        "index": 61,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Kaja"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/selena.png?w=64",
        "index": 62,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Selena"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/aldous.png?w=64",
        "index": 63,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Aldous"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/claude.png?w=64",
        "index": 64,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Claude"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/vale.png?w=64",
        "index": 65,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Vale"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/leomord.png?w=64",
        "index": 66,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Leomord"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/lunox.png?w=64",
        "index": 67,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Lunox"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/hanzo.png?w=64",
        "index": 68,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Hanzo"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/belerick.png?w=64",
        "index": 69,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Belerick"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/kimmy.png?w=64",
        "index": 70,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Kimmy"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/thamuz.png?w=64",
        "index": 71,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Thamuz"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/harith.png?w=64",
        "index": 72,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Harith"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/minsitthar.png?w=64",
        "index": 73,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Minsitthar"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/kadita.png?w=64",
        "index": 74,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Kadita"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/faramis.png?w=64",
        "index": 75,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Faramis"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/badang.png?w=64",
        "index": 76,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Badang"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/khufra.png?w=64",
        "index": 77,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Khufra"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/granger.png?w=64",
        "index": 78,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Granger"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/guinevere.png?w=64",
        "index": 79,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Guinevere"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/esmeralda.png?w=64",
        "index": 80,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Esmeralda"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/terizla.png?w=64",
        "index": 81,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Terizla"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/x-borg.png?w=64",
        "index": 82,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "X.Borg"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/ling.png?w=64",
        "index": 83,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Ling"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/dyrroth.png?w=64",
        "index": 84,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Dyrroth"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/lylia.png?w=64",
        "index": 85,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Lylia"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/baxia.png?w=64",
        "index": 86,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Baxia"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/masha.png?w=64",
        "index": 87,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Masha"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/wanwan.png?w=64",
        "index": 88,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Wanwan"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/silvanna.png?w=64",
        "index": 89,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Silvanna"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/cecilion.png?w=64",
        "index": 90,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Cecilion"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/carmilla.png?w=64",
        "index": 91,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Carmilla"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/atlas.png?w=64",
        "index": 92,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Atlas"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/popol-and-kupa.png?w=64",
        "index": 93,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Popol and Kupa"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/yu-zhong.png?w=64",
        "index": 94,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Yu Zhong"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/luo-yi.png?w=64",
        "index": 95,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Luo Yi"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/benedetta.png?w=64",
        "index": 96,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Benedetta"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/khaleed.png?w=64",
        "index": 97,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Khaleed"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/barats.png?w=64",
        "index": 98,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Barats"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/brody.png?w=64",
        "index": 99,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Brody"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/yve.png?w=64",
        "index": 100,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Yve"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/mathilda.png?w=64",
        "index": 101,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Mathilda"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/paquito.png?w=64",
        "index": 102,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Paquito"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/gloo.png?w=64",
        "index": 103,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Gloo"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/beatrix.png?w=64",
        "index": 104,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Beatrix"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/phoveus.png?w=64",
        "index": 105,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Phoveus"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/natan.png?w=64",
        "index": 106,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Natan"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/aulus.png?w=64",
        "index": 107,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Aulus"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/aamon.png?w=64",
        "index": 108,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Aamon"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/valentina.png?w=64",
        "index": 109,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Valentina"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/edith.png?w=64",
        "index": 110,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Edith"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/floryn.png?w=64",
        "index": 111,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Floryn"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/yin.png?w=64",
        "index": 112,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Yin"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/melissa.png?w=64",
        "index": 113,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Melissa"
      },
      {
        "img": "https://static.expertwm.com/mlbb/heroes/xavier.png?w=64",
        "index": 114,
        "Layout": {
          "color": "default"
        },
        "clicked": False,
        "name": "Xavier"
      }
    ],
    "chipLayout": {
      "size": "small"
    },
    "unique_id": "2553b954d349478180387afec460a945",
    "toStore": False,
    "hasChanged": True,
    "clickedChange": False,
    "equipmentCategory": [
      {
        "index": 0,
        "color": "#880808",
        "name": "Attack"
      },
      {
        "index": 1,
        "color": "#0047AB",
        "name": "Magic"
      }
    ],
    "changeTitleBtnLayout": {
      "disabled": False
    },
    "addNewHero": False,
    "numOfHeroes": [
      {
        "index": 0,
        "sum": "+2",
        "heroesUserAttachedToSet": [
          {
            "img": "https://static.expertwm.com/mlbb/heroes/miya.png?w=64",
            "index": 0,
            "Layout": {
              "color": "primary"
            },
            "clicked": True,
            "name": "Miya"
          },
          {
            "img": "https://static.expertwm.com/mlbb/heroes/balmond.png?w=64",
            "index": 1,
            "Layout": {
              "color": "primary"
            },
            "clicked": True,
            "name": "Balmond"
          }
        ],
        "expand": False,
        "threeToShow": []
      }
    ],
    "bottom3Equipment": [
      {
        "stat": "+4453",
        "index": 0,
        "name": "Health"
      },
      {
        "stat": "+589",
        "index": 1,
        "name": "Magic Power"
      },
      {
        "stat": "+33%",
        "index": 2,
        "name": "Atk Speed"
      }
    ],
    "title": "Change Name Here",
    "top3Equipment": [
      {
        "stat": "+4453",
        "index": 0,
        "name": "Health"
      },
      {
        "stat": "+589",
        "index": 1,
        "name": "Magic Power"
      },
      {
        "stat": "+33%",
        "index": 2,
        "name": "Atk Speed"
      }
    ],
    "remove": False,
    "expandData": [
      {
        "index": 0,
        "gridD": [
          {
            "value": 5,
            "stat": "5",
            "index": 0,
            "name": "Movement_Speed"
          },
          {
            "value": 8,
            "stat": "8",
            "index": 1,
            "name": "Hybrid_Lifesteal"
          },
          {
            "value": 280,
            "stat": "280",
            "index": 2,
            "name": "Magic_Power"
          },
          {
            "value": 600,
            "stat": "600",
            "index": 3,
            "name": "Mana"
          },
          {
            "value": 2750,
            "stat": "2750",
            "index": 4,
            "name": "HP"
          },
          {
            "value": 175,
            "stat": "175",
            "index": 5,
            "name": "Physical_Attack"
          },
          {
            "value": 20,
            "stat": "20",
            "index": 6,
            "name": "CD_Reduction"
          },
          {
            "value": 5,
            "stat": "5",
            "index": 7,
            "name": "Mana_Regen"
          }
        ],
        "toggle": False
      }
    ],
    "equipmentList": [
      {
        "img": "https://static.expertwm.com/mlbb/items/blade-of-the-heptaseas.png?w=64",
        "index": 0,
        "name": "Blade of the Heptaseas"
      },
      {
        "img": "https://static.expertwm.com/mlbb/items/blood-wings.png?w=64",
        "index": 1,
        "name": "Blood Wings"
      },
      {
        "img": "https://static.expertwm.com/mlbb/items/clock-of-destiny.png?w=64",
        "index": 2,
        "name": "Clock of Destiny"
      },
      {
        "img": "https://static.expertwm.com/mlbb/items/concentrated-energy.png?w=64",
        "index": 3,
        "name": "Concentrated Energy"
      },
      {
        "img": "https://static.expertwm.com/mlbb/items/endless-battle.png?w=64",
        "index": 4,
        "name": "Endless Battle"
      },
      {
        "img": "https://static.expertwm.com/mlbb/items/war-axe.png?w=64",
        "index": 5,
        "name": "War Axe"
      }
    ],
    "expand": False
  }
]
    # data[0]["index"] = 0
    # data[0]["numOfHeroes"][0]["expand"] = False
    # data[0]["numOfHeroes"][0]["sum"] = ""
    num_clicks = card_component(data=data, showAdd=True, addHeroComponent=True, showHero=True, showChartSwitch=False, saveEdits=False, EditDashboard=True, userSetRating=False, key="foo_")
    st.write(num_clicks)
