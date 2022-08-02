import { Component, OnInit } from '@angular/core';

import { FormBuilder, FormGroup } from '@angular/forms';
import { SDService } from '../sd.service';
@Component({
  selector: 'app-train',
  templateUrl: './train.component.html',
  styleUrls: ['./train.component.scss']
})
export class TrainComponent implements OnInit {

  result:any;
  form!: FormGroup;
  constructor(private formBuilder: FormBuilder, private sds:SDService) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      file: ['']
    });
  }

  onChange(event:any) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      if(this.form.get('file')!=null){
      this.form.get('file')!.setValue(file);
      }
    }
  }

  train(){ 
    const formData = new FormData();
    formData.append( 'file', new Blob([this.form.get('file')!.value], { type: 'text/csv' }), this.form.get('file')!.value.name);
    formData.append('filename',this.form.get('file')!.value.name)
    //formData.append('file', this.form.get('file')!.value);
    this.sds.train(formData ).subscribe((res:any)=>{
      this.result =res;
      this.form.reset();
      alert("trained successfully")
    },(error:any)=>{
      alert("error")
    })
    
    

  }

}
