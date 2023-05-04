import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Blog_back_CUD, Blog_Detail_R, Blog_LDS_CUD, Blog_list_R} from "./hadzen_models";

@Injectable({
  providedIn: 'root'
})
export class BlogLdsSerService {

  baseUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) { }

  putLDS(data:any): Observable<Blog_LDS_CUD[]> {
    console.log(this.http.post<Blog_LDS_CUD[]>(`${this.baseUrl}/bl/lds/`,data),);
    return this.http.post<Blog_LDS_CUD[]>(`${this.baseUrl}/bl/lds/`,data);
  }

  delLDS(id:number, us_id:number): Observable<Blog_LDS_CUD[]> {
  console.log(this.http.delete<Blog_LDS_CUD[]>(`${this.baseUrl}/bl/lds/${id}/${us_id}`));
  return this.http.delete<Blog_LDS_CUD[]>(`${this.baseUrl}/bl/lds/${id}/${us_id}`);
}

}
