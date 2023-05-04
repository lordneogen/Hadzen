import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { NewPostComponent } from './new-post/new-post.component';
import {LogRegComponent} from "./log-reg/log-reg.component";
import {PostsComponent} from "./posts/posts.component";
import {PostDetailComponent} from "./post-detail/post-detail.component";
import { ShortChannelsComponent } from './short-channels/short-channels.component';
import { ChenellBlogsComponent } from './chenell-blogs/chenell-blogs.component';
import { NewChanellComponent } from './new-chanell/new-chanell.component';
import {FormsModule} from "@angular/forms";
import { ManagerComponent } from './manager/manager.component';
import {HttpClientModule} from "@angular/common/http";

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'new-post', component: NewPostComponent },
  { path: 'new-chanell', component: NewChanellComponent },
  { path: 'update-post/:postId', component: NewPostComponent },
  { path: 'update-chanell/:postId', component: NewChanellComponent },
  { path: 'login', component: LogRegComponent },
  { path: 'posts', component: HomeComponent },
  {path: 'chanell/:postId', component: ChenellBlogsComponent},
  { path: 'posts/:postId', component: PostDetailComponent },
  { path: 'mang',component:ManagerComponent},
  { path: '', redirectTo: '/home', pathMatch: 'full' },
];

@NgModule({
  declarations: [
    AppComponent,
    TopBarComponent,
    HomeComponent,
    AboutComponent,
    NewPostComponent,
    LogRegComponent,
    PostsComponent,
    PostDetailComponent,
    ShortChannelsComponent,
    ChenellBlogsComponent,
    NewChanellComponent,
    ManagerComponent,
  ],
    imports: [
        BrowserModule,
        RouterModule.forRoot(routes),
        FormsModule,
      HttpClientModule
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
