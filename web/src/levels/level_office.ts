import Game from "../models/Game";
import Level from "../models/Level";

export const level_office: Level<undefined> = {
  id: "office",
  saveData: undefined,
  defaultPosition: "meeting_room",
  positions: [
    // 6th Floor
    {
      id: "fireexit_6_floor",
      buttons: [
        {
          id: "go_up",
          onClick: () => Game.setPosition("fireexit_7_floor"),
        },
      ],
    },

    // 7th Floor
    {
      id: "meeting_room",
      buttons: [
        {
          id: "leave",
          onClick: () => Game.setPosition("hallway_7_floor"),
        },
      ],
    },
    {
      id: "hallway_7_floor",
      buttons: [
        {
          id: "sauna",
          onClick: () => Game.setPosition("sauna_7_floor"),
        },
        {
          id: "elevator",
          onClick: () => Game.setPosition("elevator_7_floor"),
        },
        {
          id: "fireexit",
          onClick: () => Game.setPosition("fireexit_7_floor"),
        },
      ],
    },
    {
      id: "sauna_7_floor",
      buttons: [
        {
          id: "go_up",
          onClick: () => Game.setPosition("sauna_8_floor"),
        },
        {
          id: "leave",
          onClick: () => Game.setPosition("hallway_7_floor"),
        },
      ],
    },
    {
      id: "elevator_7_floor",
      buttons: [
      ],
    },
    {
      id: "fireexit_7_floor",
      buttons: [
        {
          id: "go_up",
          onClick: () => Game.setPosition("fireexit_8_floor"),
        },
        {
          id: "go_down",
          onClick: () => Game.setPosition("fireexit_6_floor"),
        },
        {
          id: "leave",
          onClick: () => Game.setPosition("hallway_7_floor"),
        }
      ],
    },

    // 8th Floor
    {
      id: "hallway_8_floor",
      buttons: [
        {
          id: "sauna",
          onClick: () => Game.setPosition("sauna_8_floor"),
        },
        {
          id: "elevator",
          onClick: () => Game.setPosition("elevator_8_floor"),
        },
        {
          id: "fireexit",
          onClick: () => Game.setPosition("fireexit_8_floor"),
        },
        {
          id: "office",
          onClick: () => Game.setPosition("office_mark"),
        },
      ],
    },
    {
      id: "sauna_8_floor",
      buttons: [
        {
          id: "go_down",
          onClick: () => Game.setPosition("sauna_7_floor"),
        },
        {
          id: "leave",
          onClick: () => Game.setPosition("hallway_8_floor"),
        }
      ],
    },
    {
      id: "elevator_8_floor",
      buttons: [
      ],
    },
    {
      id: "fireexit_8_floor",
      buttons: [
        {
          id: "go_down",
          onClick: () => Game.setPosition("fireexit_7_floor"),
        },
        {
          id: "leave",
          onClick: () => Game.setPosition("hallway_8_floor"),
        },
      ],
    },
    {
      id: "office_mark",
      buttons: [
        {
          id: "grab_items",
          onClick: () => {
            console.error("WIP, grab item logic");
          },
        },
        {
          id: "leave",
          onClick: () => Game.setPosition("hallway_8_floor"),
        },
      ],
    },
  ],
};