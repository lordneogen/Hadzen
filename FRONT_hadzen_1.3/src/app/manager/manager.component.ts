import { Component } from '@angular/core';
import {Channel_CRUD} from "../hadzen_models";
import {chanell_list} from "../chanell";
import {ChanellSerService} from "../chanell-ser.service";
import {Location} from "@angular/common";
import {ActivatedRoute, Router} from "@angular/router";
import {MangSerService} from "../mang-ser.service";

@Component({
  selector: 'app-manager',
  templateUrl: './manager.component.html',
  styleUrls: ['./manager.component.css']
})
export class ManagerComponent {

  chanells:Channel_CRUD [] = chanell_list;

  email:number=0;
  ch:number=0;
  create_field:boolean=false;

  update_field:boolean=false;

  delete_comm:boolean=false;

  us_id:number=0;

  ch_id:number=0;
  red_ch:boolean=false;

  constructor(private manser:MangSerService) {
  }

  putMang(){
        let data={
          email:this.us_id,
          ch:this.ch_id,
          create_field:this.create_field,
          delete_comm:this.delete_comm,
          update_field:this.update_field,
          red_ch:this.red_ch
        }
        this.manser.putMang(
          data
        ).subscribe(
          (response) => console.log(response),
          (error) => console.log(error)
        );
  }

}

