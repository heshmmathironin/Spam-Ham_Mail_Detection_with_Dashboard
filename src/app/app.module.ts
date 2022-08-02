import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule,ReactiveFormsModule  } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TrainComponent } from './train/train.component';
import { PredictComponent } from './predict/predict.component';
import { BulkpredictComponent } from './bulkpredict/bulkpredict.component';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    TrainComponent,
    PredictComponent,
    BulkpredictComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,ReactiveFormsModule ,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
