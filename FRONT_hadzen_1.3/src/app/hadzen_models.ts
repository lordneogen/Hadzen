export interface Channel_CRUD {
  id:number;
  name:string;
  img:string;
  title:string;
  date:Date;
  is_comm:boolean;
  owner:number;
}
export interface Blog_back_CUD {
  id:number;
  name:string;
  text_in:string;
  date:Date;
  img:string;
  creator:number;
  ch:number;
}
export interface Blog_list_R {
  chanell:string;
  img:string;
  subs:number;
  blog_detail:Blog_back_CUD;
  like_count:number;
  dis_count:number;
  share_count:number;
}
export interface Comments_back_CUD {
  id:number;
  text:string;
  date:Date;
  user:number;
  bl:number;
}
export interface Comm_LD_CUD {
  id:number;
  is_like:boolean;
  is_dis:boolean;
  user:number;
  comm:number;
}
export interface Blog_LDS_CUD {
  id:number;
  is_like:boolean;
  is_dis:boolean;
  is_share:boolean;
  user:number;
  bl:number;
}
export interface Manager_CRUD {
  create_field:boolean;
  update_field:boolean;
  delete_comm:boolean;
  red_ch:boolean;
  email:number;
  ch:number;

}
export interface Comm_min_R {
  //     "user": "hh",
//     "text": "text",
//     "date": "2023-04-20T08:21:41.945490Z",
//     "like": 1,
//     "dis": 0
  user:string;
  text:string;
  date:Date;
  like:number;
  dis:number;
}
export interface Blog_Detail_R {
  channel:string;
  img:string;
  subs:number;
  blog_detail:Blog_back_CUD;
  like_count:number;
  dis_count:number;
  share_count:number;
  comments:Comm_min_R[];
}
