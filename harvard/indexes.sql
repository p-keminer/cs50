CREATE INDEX "enrollmentsx" ON "enrollments" ("student_id");
CREATE INDEX "enrollmentsxx" ON "enrollments" ("course_id");
CREATE INDEX "coursesx" ON "courses" ("department","number","semester");
CREATE INDEX "coursesxx" ON "courses" ("semester");
CREATE INDEX "satisfiesx" ON "satisfies" ("course_id");
