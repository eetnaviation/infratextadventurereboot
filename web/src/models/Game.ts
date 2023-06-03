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

  static init() {
    this.createDefaultSave();
  }

  static createDefaultSave() {
    setState({
      level: level_office,
      position: level_office.positions.find(p => p.id == level_office.defaultPosition),
    });
  }

  static setLevel(level: Level<any>) {
    setState({
      level: level,
    });
  }

  static setPosition(id: string) {
    if (state.level == undefined) throw new Error("Illegal state. Level is undefined but trying to set position");
    setState({
      position: state.level!.positions.find(p => p.id == id),
    });
  }

  static setLevelAndPosition(level: Level<any>, position: string) {
    setState({
      level: level,
      position: level.positions.find(p => p.id == position),
    });
  }
}