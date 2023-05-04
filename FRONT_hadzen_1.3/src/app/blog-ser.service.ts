import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Blog_back_CUD, Blog_Detail_R, Blog_list_R, Channel_CRUD} from "./hadzen_models";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class BlogSerService {



  baseUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) { }

  getBlogs(): Observable<Blog_list_R[]> {
    console.log(this.http.get<Blog_list_R[]>(`${this.baseUrl}/bl/`));
    return this.http.get<Blog_list_R[]>(`${this.baseUrl}/bl/`);
  }

  getBlogDetail(id:number): Observable<Blog_Detail_R> {
    console.log(`${this.baseUrl}/bl/${id}/`);
    return this.http.get<Blog_Detail_R>(`${this.baseUrl}/bl/${id}/`);
  }

  getChanellBlogs(id:number): Observable<Blog_list_R[]> {
    console.log(`${this.baseUrl}/ch/${id}/bl`);
    return this.http.get<Blog_list_R[]>(`${this.baseUrl}/ch/${id}/bl`);
  }

  putBl(data: any) {
    return this.http.post<Blog_back_CUD[]>(`${this.baseUrl}/blm/`,data);
  }

  deleteBl(id: number) {
     return this.http.delete<Blog_back_CUD[]>(`${this.baseUrl}/blm/${id}/`);
  }

  updateBl(id: number,data:any) {
    return this.http.put<Blog_back_CUD[]>(`${this.baseUrl}/blm/${id}/`,data);
  }
}
