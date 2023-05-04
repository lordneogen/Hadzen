import { Component } from '@angular/core';
import {Blog_back_CUD} from "../hadzen_models";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-log-reg',
  templateUrl: './log-reg.component.html',
  styleUrls: ['./log-reg.component.css']
})
export class LogRegComponent {
  showLogin = true;
  showRegister = false;


// {
//   "username": "gorno",
//   "email": "dlkfdklfdl@sdjsojkjkf.ru",
//   "first_name": "jojo",
//   "last_name": "jojo"
// }
  username:string="";

  email:string="";

  password:string="";

  password2:string="";

  first_name:string="fname";

  last_name:string="lname";

  baseUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) { }

  putUser() {

    let data={
      username:this.username,
      email:this.email,
      password:this.password,
      password2:this.password2,
      first_name:this.first_name,
      last_name:this.last_name
    }
    return this.http.post<any>(`${this.baseUrl}/register/`,data).subscribe(
      (response) => console.log(response),
      (error) => console.log(error)
    );;
  }

}
