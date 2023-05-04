import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { map } from 'rxjs/operators';
import {Blog_Detail_R, Blog_list_R} from "../hadzen_models";
import {blog_detail} from "../blog_detail";
import {blog_list} from "../blog_list";
import {BlogSerService} from "../blog-ser.service";
import {BlogLdsSerService} from "../blog-lds-ser.service";
import {ComSerService} from "../com-ser.service";

@Component({
  selector: 'app-post-detail',
  templateUrl: './post-detail.component.html',
  styleUrls: ['./post-detail.component.css']
})
export class PostDetailComponent implements OnInit {
  myId: number =0;

  ChId:number=0;

  blog: any |undefined;

  blogs: any|undefined;

  user:number=1;

  text:string="";



  constructor(private route: ActivatedRoute,
              private blogService: BlogSerService,
              private blogLDSSer:BlogLdsSerService,

              private commSer:ComSerService) {
  }

  BlogDel(){
     this.blogService.deleteBl(this.myId).subscribe(
       () => console.log('Object deleted successfully'),
       error => console.error('Error deleting object:', error)
     );
    location.assign('http://localhost:4200/home');
  }

  BlogUpd(){
    let url_up="http://localhost:4200/update-post/"+this.myId;
    console.log(url_up)
    location.assign(url_up);
  }

  ngOnInit() {
    this.route.params.pipe(
      map(params => parseInt(params['postId'], 0))
    ).subscribe(id => {
      this.myId = id;
      this.blogService.getBlogDetail(id).subscribe((blogs_r) => {
        this.blog = blogs_r;
        this.ChId = blogs_r.blog_detail.ch
        this.blogService.getChanellBlogs(blogs_r.blog_detail.ch).subscribe((blogs_r1) => {
          this.blogs = blogs_r1;
        });
      });
    });
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

  sendComm() {
    const data = {text:this.text,user:this.user,bl:this.myId};
    console.log(data);
    this.commSer.putCom(data).subscribe(
      (response) => console.log(response))
  }
}
