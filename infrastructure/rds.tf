locals {
  database_username = "postgres"
}

resource "aws_db_instance" "aion_nexus" {
  identifier             = "aion-nexus"
  allocated_storage      = 20
  max_allocated_storage  = 1000
  engine                 = "postgres"
  engine_version         = "14"
  instance_class         = "db.t4g.micro"
  db_name                = "spamoverflow"
  username               = local.database_username
  password               = random_password.password.result
  parameter_group_name   = "default.postgres14"
  skip_final_snapshot    = true
  vpc_security_group_ids = [aws_security_group.aion_nexus.id]
  publicly_accessible    = true
  tags = {
    Name = "aion_nexus_database"
  }
}

resource "random_password" "password" {
  length  = 16
  special = false
}

resource "aws_security_group" "aion_nexus" {
  name        = "aion_nexus_database"
  description = "Allow inbound Postgresql traffic"
  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
  tags = {
    Name = "aion_nexus_database"
  }
}
