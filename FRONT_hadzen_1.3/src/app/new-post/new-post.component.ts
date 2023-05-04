import {Component, OnInit} from '@angular/core';
import {Blog_back_CUD, Channel_CRUD} from "../hadzen_models";
import {chanell_list} from "../chanell";
import {ChanellSerService} from "../chanell-ser.service";
import {BlogSerService} from "../blog-ser.service";
import { Location } from '@angular/common';
import {ActivatedRoute, Router} from "@angular/router";
import {map} from "rxjs/operators";
@Component({
  selector: 'app-new-post',
  templateUrl: './new-post.component.html',
  styleUrls: ['./new-post.component.css']
})
export class NewPostComponent implements OnInit{


  url="";

  constructor(private myService: ChanellSerService,private blogService:BlogSerService,private location: Location,  private route: ActivatedRoute,
              private router: Router) {}

  name:string="";
  text_in:string|undefined;
  date:Date=new Date();
  img:string="";

  data:any|undefined;
  id_up:number=0;

  rt:any|undefined;
  creator:number|undefined;

  ch:string="";


  myFunction() {
    console.log(this.name+' '+this.text_in+' '+this.img);
  }

  chanells: Channel_CRUD[] = [];


  getBlogs() {
    this.myService.getChanells().subscribe((ch_r) => {
      this.chanells = ch_r;
    });
  }


  sendData() {

    const regex = /\d+/; // Регулярное выражение для поиска чисел в тексте
    const match = this.ch.match(regex); // Ищем первое число в тексте
    if (match) {
      const firstNumber = parseInt(match[0], 10); // Конвертируем первое число в number
      console.log(firstNumber);
      const data = { name: this.name, text_in:this.text_in,img:this.img,creator:1,ch:firstNumber};
      this.blogService.putBl(data).subscribe(
        (response) => console.log(response),
        (error) => console.log(error)
      );
      location.assign('http://localhost:4200/home');
    } else {
      console.log("Число не найдено в тексте");
    }
  }



  ngOnInit(): void {
    this.url = this.location.path(); // получение текущего адреса ссылки
    console.log(this.url);
    if(this.url.indexOf("update")!=-1){
      this.route.params.pipe(
        map(params => parseInt(params['postId'], 0))
      ).subscribe(id => {
        this.id_up = id;
        this.blogService.getBlogDetail(id).subscribe((blogs_r) => {
          this.name = blogs_r.blog_detail.name;
          this.img=blogs_r.blog_detail.img;
          // this.url = blogs_r.blog_detail.img;
          this.text_in = blogs_r.blog_detail.text_in;
        });
        console.log(id)
      });

    }
    this.getBlogs()
  }

  updatebl() {
    this.data={
      name:this.name,
      text_in:this.text_in,
      img:this.img
    };
    this.blogService.updateBl(this.id_up,this.data).subscribe(
      (response) => console.log(response),
      (error) => console.log(error)
    );
    location.assign('http://localhost:4200/home');
  }

}
