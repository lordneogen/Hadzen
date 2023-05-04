import {blog} from "./blog";
// user:string;
// text:string;
// date:Date;
// like:number;
// dis:number;
export const blog_detail=[

  {
    channel:"Такого блога не найдено",
    img:"assets/Bufotes_oblongus.jpg",
    subs:0,
    blog_detail:blog[0],
    like_count:0,
    dis_count:0,
    share_count:0,
    comments:[]
  },
  {
    channel:"Все о лягушках",
    img:"assets/Bufotes_oblongus.jpg",
    subs:1,
    blog_detail:blog[0],
    like_count:0,
    dis_count:0,
    share_count:0,
    comments:[
      {
        user:"jojo",
        text:"Крутой пост",
        date: new Date('2022-04-22T10:00:00'),
        like:0,
        dis:0
      }
    ]
  }
]
