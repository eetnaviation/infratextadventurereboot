import { createStore } from "solid-js/store";
import { level_menu, position_menu_menu } from "../levels/menu";
import Level from "./Level";

const [data, setData] = createStore({
  level: level_menu,
  position: position_menu_menu,
});

export default class Game {

  static readonly data = data;

  static setLevel(level: Level<any>) {
    setData({
      level,
    });
    //setData("level", level);
  }

  static setPosition(id: string) {
    const position = data.level.positions.find(pos => pos.id == id);
    if (position != undefined) setData({
      position,
    });
  }
}