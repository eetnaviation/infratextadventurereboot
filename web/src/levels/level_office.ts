import Level from "../models/Level";

export const level_office: Level<undefined> = {
  id: "office",
  saveData: undefined,
  defaultPosition: "meeting_room",
  positions: [
    {
      id: "meeting_room",
      buttons: [
        {
          id: "next_slide",
          onClick: () => {

          },
        },
      ],
    },
  ],
};