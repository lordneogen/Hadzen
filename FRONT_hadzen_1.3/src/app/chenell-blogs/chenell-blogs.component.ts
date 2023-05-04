import {Component, OnInit} from '@angular/core';
import {Blog_list_R, Channel_CRUD, Manager_CRUD} from "../hadzen_models";
import {blog_list} from "../blog_list";
import {chanell_list} from "../chanell";
import {ActivatedRoute} from "@angular/router";
import {map} from "rxjs/operators";
import {blog_detail} from "../blog_detail";
import {BlogSerService} from "../blog-ser.service";
import {ChanellSerService} from "../chanell-ser.service";
import {BlogLdsSerService} from "../blog-lds-ser.service";
import {MangSerService} from "../mang-ser.service";

@Component({
  selector: 'app-chenell-blogs',
  templateUrl: './chenell-blogs.component.html',
  styleUrls: ['./chenell-blogs.component.css']
})
export class ChenellBlogsComponent implements OnInit{
  myId: number =0;

  blogs: any |undefined;

  chanell: any;

  man:boolean=false;

  managers:Manager_CRUD[]=[];
  constructor(private route: ActivatedRoute,
              private blogService: BlogSerService,
              private chSer:ChanellSerService,
              private blogLDSSer:BlogLdsSerService,

              private managerSer:MangSerService) {
  }

  ngOnInit() {
    this.route.params.pipe(
      map(params => parseInt(params['postId'], 0))
    ).subscribe(id => {
      this.myId = id;
      this.chSer.getChanellsbyId(id).subscribe((ch_r) => {
        this.chanell = ch_r[0];
      });
      this.blogService.getChanellBlogs(id).subscribe((blogs_r) => {
        this.blogs = blogs_r;
      });

    });
    this.managerSer.getMang(this.myId).subscribe((blogs_r) => {
      this.managers = blogs_r;
    });
  }

  ChDel(){
    this.chSer.deleteCh(this.myId).subscribe(
      () => console.log('Object deleted successfully'),
      error => console.error('Error deleting object:', error)
    );
    location.assign('http://localhost:4200/home');
  }

  sendLDS(id:number,type:number) {
    const data = {is_like:type==1,is_dis:type==2,is_share:type==3,user:1,bl:id};
    console.log(data);
    this.blogLDSSer.putLDS(data).subscribe(
      (response) => console.log(response))
    this.blogLDSSer.delLDS(data.bl,1).subscribe(
      (response) =>     this.blogLDSSer.putLDS(data).subscribe(
        (response) => console.log(response)
      ),
      (error) =>console.log(error)
    )
  }

  upd(){
    location.assign('http://localhost:4200/update-chanell/'+this.chanell.id);
  }
  mang(){
    this.man=!this.man
  }
}
