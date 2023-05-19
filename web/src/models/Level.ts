import Position from "./Position";

export default interface Level<LevelData> {
  readonly id: string;
  readonly saveData: LevelData;
  readonly positions: Position[];
  readonly onEnter?: () => void;
  readonly onLeave?: () => void;
  readonly onChangePosition?: () => void;
}