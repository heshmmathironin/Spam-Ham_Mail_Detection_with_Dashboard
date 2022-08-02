import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BulkpredictComponent } from './bulkpredict.component';

describe('BulkpredictComponent', () => {
  let component: BulkpredictComponent;
  let fixture: ComponentFixture<BulkpredictComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BulkpredictComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BulkpredictComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
