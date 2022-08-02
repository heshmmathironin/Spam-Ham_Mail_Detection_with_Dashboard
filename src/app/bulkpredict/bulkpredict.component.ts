import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { SDService } from '../sd.service';
import {saveAs} from "file-saver";
//var FileSaver = require('file-saver');
@Component({
  selector: 'app-bulkpredict',
  templateUrl: './bulkpredict.component.html',
  styleUrls: ['./bulkpredict.component.scss']
})
export class BulkpredictComponent implements OnInit {
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

  bulkpredict(){ 
    const formData = new FormData();
    formData.append( 'file', new Blob([this.form.get('file')!.value], { type: 'text/csv' }), this.form.get('file')!.value.name);
    formData.append('filename',this.form.get('file')!.value.name)
    //formData.append('file', this.form.get('file')!.value);
    this.sds.bulkpredict(formData ).subscribe((res:any)=>{
    
    
      const a = document.createElement('a');
      const blob = new Blob([res], { type: 'text/csv' });
   

a.href = URL.createObjectURL(blob);
a.download = 'result.csv';
a.click();
      
    },(error:any)=>{
      alert("error")
    })
    
    

  }

}
  
