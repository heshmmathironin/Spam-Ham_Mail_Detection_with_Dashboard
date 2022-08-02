import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { SDService } from '../sd.service';

@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.scss']
})
export class PredictComponent implements OnInit {
  inputText:any;
  predicted_result:any;
  constructor(private sds:SDService) { }

  ngOnInit(): void {
  }
  predict(){ 
    this.sds.predict(this.inputText ).subscribe((res:any)=>{
      this.predicted_result  =JSON.parse(res).data;
    },(error:any)=>{
      alert("error")
    })

  } 
}
