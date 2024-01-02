import { createStore } from "solid-js/store";
import Level from "./Level";
import { createContext } from "solid-js";
import Position from "./Position";
import { level_office } from "../levels/level_office";

const [state, setState] = createStore<{
  level?: Level<any>;
  position?: Position;
}>({});

export default class Game {

  static readonly state = state;
  static readonly LEVELS: { [id: string]: Level<any> } = {
    "office": level_office,
  };

  static init() {
    if (localStorage.getItem("save")) this.loadGame();
    else this.createDefaultSave();
  }

  static createDefaultSave() {
    setState({
      level: level_office,
      position: level_office.positions.find(p => p.id == level_office.defaultPosition),
    });
    this.saveGame();
  }

  static setLevel(level: Level<any>) {
    setState({
      level: level,
    });
    this.saveGame();
  }

  static setPosition(id: string) {
    const pos = state.level!.positions.find(p => p.id == id);
    console.log(`Setting position: ${id}: ${JSON.stringify(pos)}`);
    if (state.level == undefined) throw new Error("Illegal state. Level is undefined but trying to set position");
    setState({
      position: state.level!.positions.find(p => p.id == id),
    });
    this.saveGame();
  }

  static setLevelAndPosition(level: Level<any>, position: string) {
    setState({
      level: level,
      position: level.positions.find(p => p.id == position),
    });
    this.saveGame();
  }

  static saveGame() {
    localStorage.setItem("save", Date.now().toString());
    localStorage.setItem("save-level", state.level?.id as string);
    localStorage.setItem("save-position", state.position?.id as string);
  }

  static loadGame() {
    const level = this.LEVELS[localStorage.getItem("save-level")!];
    const position = localStorage.getItem("save-position");
    setState({
      level: level,
      position: level.positions.find(p => p.id == position),
    });
  }
}