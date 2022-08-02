import { TestBed } from '@angular/core/testing';

import { SDService } from './sd.service';

describe('SDService', () => {
  let service: SDService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SDService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
