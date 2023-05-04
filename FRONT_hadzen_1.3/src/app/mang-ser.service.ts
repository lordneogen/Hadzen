import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Blog_list_R, Manager_CRUD} from "./hadzen_models";

@Injectable({
  providedIn: 'root'
})
export class MangSerService {

  baseUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) { }

  getMang(id:number): Observable<Manager_CRUD[]> {
    console.log(this.http.get<Manager_CRUD[]>(`${this.baseUrl}/mn/ch/${id}`));
    return this.http.get<Manager_CRUD[]>(`${this.baseUrl}/mn/ch/${id}`);
  }
  getUs(id:string): Observable<any> {
    console.log(this.http.get<any>(`${this.baseUrl}/us/${id}`));
    return this.http.get<any>(`${this.baseUrl}/us/${id}`);
  }

  putMang(data:Manager_CRUD): Observable<Manager_CRUD> {
    console.log(this.http.get<Manager_CRUD>(`${this.baseUrl}/mn/`));
    return this.http.post<Manager_CRUD>(`${this.baseUrl}/mn/`,data);
  }
}
