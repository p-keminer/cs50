DROP TRIGGER "log_user_updates";
DROP TRIGGER "log_user_deletes";
DROP TRIGGER "log_user_inserts";




UPDATE "users" SET "password" = (
    "982c0381c279d139fd221fce974916e7"
)WHERE "username" = "admin";



INSERT INTO "user_logs" ("type","old_username","new_username","old_password","new_password")
VALUES
('update','admin','admin','e10adc3949ba59abbe56e057f20f883e','44bf025d27eea66336e5c1133c3827f7');






CREATE TRIGGER "log_user_updates"
AFTER UPDATE OF "username", "password" ON "users"
FOR EACH ROW
BEGIN
    INSERT INTO "user_logs" ("type", "old_username", "new_username", "old_password", "new_password")
    VALUES ('update', OLD."username", NEW."username", OLD."password", NEW."password");
END;
CREATE TRIGGER "log_user_deletes"
AFTER DELETE ON "users"
FOR EACH ROW
BEGIN
    INSERT INTO "user_logs" ("type", "old_username", "new_username", "old_password", "new_password")
    VALUES ('delete', OLD."username", NULL, OLD."password", NULL);
END;
CREATE TRIGGER "log_user_inserts"
AFTER INSERT ON "users"
FOR EACH ROW
BEGIN
    INSERT INTO "user_logs" ("type", "old_username", "new_username", "old_password", "new_password")
    VALUES ('insert', NULL, NEW."username", NULL, NEW."password");
END;
