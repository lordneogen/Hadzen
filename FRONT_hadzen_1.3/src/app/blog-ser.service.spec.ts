import { TestBed } from '@angular/core/testing';

import { BlogSerService } from './blog-ser.service';

describe('BlogSerService', () => {
  let service: BlogSerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BlogSerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
