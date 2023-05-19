import Game from "../models/Game";
import Level from "../models/Level";

export const level_menu: Level<{}> = {
  id: "menu",
  saveData: {},
  positions: [
    {
      id: "menu",
      buttons: [
        {
          id: "load_game",
          onClick: () => Game.setPosition("load_game"),
        },
      ],
    },
    {
      id: "load_game",
      buttons: [
        {
          id: "slot_1",
          onClick: () => {},
        },
        {
          id: "slot_2",
          onClick: () => {},
        },
        {
          id: "slot_3",
          onClick: () => {},
        },
        {
          id: "slot_4",
          onClick: () => {},
        },
        {
          id: "back",
          onClick: () => Game.setPosition("menu"),
        },
      ],
    },
  ],
};
export const position_menu_menu = level_menu.positions[0];