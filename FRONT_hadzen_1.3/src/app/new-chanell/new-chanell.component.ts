import {Component, NgModule, OnInit} from '@angular/core';
import { FormsModule } from '@angular/forms';
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";
import {ChanellSerService} from "../chanell-ser.service";
import {map} from "rxjs/operators";
import {Location} from "@angular/common";
import {ActivatedRoute, Router} from "@angular/router";
@Component({
  selector: 'app-new-chanell',
  templateUrl: './new-chanell.component.html',
  styleUrls: ['./new-chanell.component.css']
})
export class NewChanellComponent implements OnInit{
  name:string|undefined;
  title:string|undefined;
  is_comm:boolean=true;
  owner:number|undefined;
  img:string="";

  data:any|undefined;

  id_up:number=0;

  url:string="";

  query = '';
  results: any[]|undefined;
  myFunction() {
    console.log(this.name+' '+this.title+' '+this.img);
  }

  constructor(private myService: ChanellSerService,private location: Location,  private route: ActivatedRoute,
              private router: Router) {}

  ngOnInit(): void {
    this.url = this.location.path(); // получение текущего адреса ссылки
    console.log(this.url);
    if(this.url.indexOf("update")!=-1){
      this.route.params.pipe(
        map(params => parseInt(params['postId'], 0))
      ).subscribe(id => {
        this.id_up = id;
        this.myService.getChanellsbyId(id).subscribe((blogs_r) => {
          this.name = blogs_r[0].name;
          this.img=blogs_r[0].img;
          this.title=blogs_r[0].title
        });
        console.log(id)
      });

    }
    }

  sendData() {
    const data = { name: this.name, title:this.title,is_comm:true,owner:1,img:this.img };
    this.myService.putCh(data).subscribe(
      (response) => console.log(response),
      (error) => console.log(error)
    );
    location.assign('http://localhost:4200/home');
  }

  updatech() {
    this.data={
      name:this.name,
      img:this.img,
      title:this.title
    };

    this.myService.updateCh(this.id_up,this.data).subscribe(
      (response) => console.log(response),
      (error) => console.log(error)
    );
    location.assign('http://localhost:4200/home');
  }
}
