import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Blog_back_CUD, Blog_Detail_R, Blog_list_R, Comments_back_CUD} from "./hadzen_models";

@Injectable({
  providedIn: 'root'
})
export class ComSerService {

  baseUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) { }


  putCom(data: any) {
    return this.http.post<Comments_back_CUD>(`${this.baseUrl}/cm/`,data);
  }
}
