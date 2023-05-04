import {ChangeDetectorRef, Component, NgModule, OnInit} from '@angular/core';
import { Post, posts} from "../posts";
import {Blog_list_R} from "../hadzen_models";
import {blog_list} from "../blog_list";
import {BlogSerService} from "../blog-ser.service";
import {BlogLdsSerService} from "../blog-lds-ser.service";
import {JwtModule} from "@auth0/angular-jwt";

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css']
})


export class PostsComponent implements OnInit {


  blogs: Blog_list_R[] = [];

  dictionary: { [key: number]: number } = {};

  constructor(private blogService: BlogSerService,private blogLDSSer:BlogLdsSerService,private cdr: ChangeDetectorRef) {
  }
  ngOnInit(): void {
    this.getBlogs();
  }

  getBlogs() {
    this.blogService.getBlogs().subscribe((blogs_r) => {
      this.blogs = blogs_r;
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
}
