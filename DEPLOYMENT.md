# E-Consultation Insight Engine - Deployment Guide

This guide provides instructions for deploying the E-Consultation Insight Engine in both development and production environments.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Quick Start (Development)](#quick-start-development)
- [Production Deployment](#production-deployment)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Scaling](#scaling)
- [Monitoring](#monitoring)
- [Backup and Recovery](#backup-and-recovery)
- [Troubleshooting](#troubleshooting)

## Prerequisites

- Docker 20.10+ and Docker Compose 1.29+
- At least 4GB RAM (8GB recommended for production)
- At least 10GB free disk space
- Domain name with DNS access (for production)
- SMTP server credentials (for email notifications)

## Quick Start (Development)

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/e-consultation-insight-engine.git
   cd e-consultation-insight-engine
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

3. **Start the services**
   ```bash
   docker-compose up -d
   ```

4. **Initialize the database**
   ```bash
   docker-compose exec api python -m backend.app.initial_data
   ```

5. **Access the application**
   - Frontend: http://localhost:8501
   - API Docs: http://localhost:8000/docs
   - Admin Email: admin@econsultation.gov
   - Admin Password: admin123 (change this immediately after first login)

## Production Deployment

### 1. Server Setup

1. **Provision a server** with your preferred cloud provider (AWS, GCP, Azure, etc.)
   - Minimum: 2 vCPUs, 4GB RAM, 50GB SSD
   - Recommended: 4 vCPUs, 8GB RAM, 100GB SSD

2. **Install Docker and Docker Compose**
   ```bash
   # Install Docker
   curl -fsSL https://get.docker.com -o get-docker.sh
   sh get-docker.sh
   
   # Install Docker Compose
   sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Configure DNS

1. Set up DNS records for your domain:
   - `sentiment.yourdomain.com` → Server IP
   - `api.sentiment.yourdomain.com` → Server IP

### 3. Configure Environment

1. **Copy and edit the environment file**
   ```bash
   cp .env.example .env.production
   nano .env.production
   ```
   
   Update at least these variables:
   ```
   APP_ENV=production
   DEBUG=false
   SECRET_KEY=generate-a-secure-key
   JWT_SECRET_KEY=generate-a-secure-jwt-key
   DATABASE_URL=postgresql://postgres:your-secure-password@db:5432/sentiment_engine
   REDIS_PASSWORD=your-secure-redis-password
   SMTP_* (configure your email settings)
   ```

### 4. Start the Services

1. **Start the stack**
   ```bash
   docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
   ```

2. **Initialize the database**
   ```bash
   docker-compose -f docker-compose.yml -f docker-compose.prod.yml exec api python -m backend.app.initial_data
   ```

3. **Verify services**
   ```bash
   docker-compose -f docker-compose.yml -f docker-compose.prod.yml ps
   docker-compose -f docker-compose.yml -f docker-compose.prod.yml logs -f
   ```

## Configuration

### Environment Variables

See [.env.example](.env.example) for all available configuration options.

### Traefik Configuration

Traefik is used as a reverse proxy with automatic Let's Encrypt certificate generation. Configuration is in `traefik/dynamic/middlewares.yml`.

## Database Setup

### Backup Database
```bash
docker exec -t postgres pg_dumpall -c -U postgres > backup_$(date +%Y-%m-%d_%H_%M_%S).sql
```

### Restore Database
```bash
cat backup_file.sql | docker exec -i postgres psql -U postgres
```

## Scaling

### Horizontal Scaling
To scale the API service:
```bash
docker-compose up -d --scale api=4
```

### Database Replication
For production, consider setting up PostgreSQL with replication:
1. Primary/standby setup
2. Connection pooling with PgBouncer
3. Regular backups

## Monitoring

### Logs
View logs with:
```bash
docker-compose logs -f
```

### Metrics
Prometheus and Grafana can be added by uncommenting the services in `docker-compose.monitoring.yml`.

## Backup and Recovery

### Regular Backups
1. Database dumps
2. File uploads directory
3. Configuration files

### Recovery Process
1. Restore database from backup
2. Restore file uploads
3. Update configuration
4. Restart services

## Troubleshooting

### Common Issues

1. **Port conflicts**
   - Check if ports 80 and 443 are free
   ```bash
   sudo lsof -i :80
   sudo lsof -i :443
   ```

2. **Certificate generation**
   - Check Traefik logs for Let's Encrypt issues
   - Ensure DNS is properly configured

3. **Database connection**
   - Verify PostgreSQL is running
   - Check connection string in .env file

### Getting Help

For support, please open an issue on GitHub or contact support@yourdomain.com.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
