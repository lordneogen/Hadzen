import {Component, OnInit} from '@angular/core';
import {Blog_list_R, Channel_CRUD} from "../hadzen_models";
import {blog_list} from "../blog_list";
import {chanell_list} from "../chanell";
import {BlogSerService} from "../blog-ser.service";
import {ChanellSerService} from "../chanell-ser.service";

@Component({
  selector: 'app-short-channels',
  templateUrl: './short-channels.component.html',
  styleUrls: ['./short-channels.component.css']
})
export class ShortChannelsComponent implements OnInit{


  chs: Channel_CRUD[] = [];


  constructor(private chService: ChanellSerService) {
  }
  ngOnInit(): void {
    this.getBlogs();
  }

  getBlogs() {
    this.chService.getChanells().subscribe((ch_r) => {
      this.chs = ch_r;
    });
  }

}
