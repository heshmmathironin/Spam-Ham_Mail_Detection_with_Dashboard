import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class SDService {

  constructor(private http:HttpClient) { }

   train(formdata:any):Observable<any>{
     alert(formdata.get('file').name)
     return this.http.post('http://localhost:8000/api/train/',formdata)

   }
 
   bulkpredict(formdata:any):Observable<any>{
   
    return this.http.post('http://localhost:8000/api/bulkpredict/',formdata,{responseType: 'blob' })

  }

  predict(inputText:any):Observable<any>{
    let formdata=new FormData();
    formdata.append('mail',inputText)
    return this.http.post('http://localhost:8000/api/predict/',formdata,{responseType:'text'})

  }
}
