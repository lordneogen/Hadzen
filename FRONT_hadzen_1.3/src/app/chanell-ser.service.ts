import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Blog_back_CUD, Channel_CRUD} from "./hadzen_models";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class ChanellSerService {



  baseUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) { }

  getChanells(): Observable<Channel_CRUD[]> {
    console.log(this.http.get<Channel_CRUD[]>(`${this.baseUrl}/ch/`));
    return this.http.get<Channel_CRUD[]>(`${this.baseUrl}/ch/`);
  }
  getChanellsbyId(id:number): Observable<Channel_CRUD[]> {
    console.log(this.http.get<Channel_CRUD[]>(`${this.baseUrl}/ch/${id}`));
    return this.http.get<Channel_CRUD[]>(`${this.baseUrl}/ch/${id}`);
  }

  putCh(data: any) {
    return this.http.post<Channel_CRUD[]>(`${this.baseUrl}/ch/`,data);
  }

  deleteCh(id: number) {
    return this.http.delete<Channel_CRUD[]>(`${this.baseUrl}/ch/${id}/`);
  }

  updateCh(id: number, data:any) {
    return this.http.put<Channel_CRUD>(`${this.baseUrl}/ch/${id}/`,data);
  }
}
