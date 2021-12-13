---
layout: post
title:  "Spring 中一些常量"
category: "Spring"
tags: ["spring", "Constants"]
date: 2019-12-04 00:00:00
updated: 2019-12-04 00:00:00
---

本文列举了 Spring 中一些常量。

<!-- more -->

### 1.StandardCharsets

```java
import java.nio.charset.StandardCharsets;

/**
 * Seven-bit ASCII, a.k.a. ISO646-US, a.k.a. the Basic Latin block of the
 * Unicode character set
 */
public static final Charset US_ASCII = Charset.forName("US-ASCII");
/**
 * ISO Latin Alphabet No. 1, a.k.a. ISO-LATIN-1
 */
public static final Charset ISO_8859_1 = Charset.forName("ISO-8859-1");
/**
 * Eight-bit UCS Transformation Format
 */
public static final Charset UTF_8 = Charset.forName("UTF-8");
/**
 * Sixteen-bit UCS Transformation Format, big-endian byte order
 */
public static final Charset UTF_16BE = Charset.forName("UTF-16BE");
/**
 * Sixteen-bit UCS Transformation Format, little-endian byte order
 */
public static final Charset UTF_16LE = Charset.forName("UTF-16LE");
/**
 * Sixteen-bit UCS Transformation Format, byte order identified by an
 * optional byte-order mark
 */
public static final Charset UTF_16 = Charset.forName("UTF-16");
```


### 2.HttpHeaders

```java
import org.springframework.http.HttpHeaders;

public static final String ACCEPT = "Accept";
public static final String ACCEPT_CHARSET = "Accept-Charset";
public static final String ACCEPT_ENCODING = "Accept-Encoding";
public static final String ACCEPT_LANGUAGE = "Accept-Language";
public static final String ACCEPT_RANGES = "Accept-Ranges";
public static final String ACCESS_CONTROL_ALLOW_CREDENTIALS = "Access-Control-Allow-Credentials";
public static final String ACCESS_CONTROL_ALLOW_HEADERS = "Access-Control-Allow-Headers";
public static final String ACCESS_CONTROL_ALLOW_METHODS = "Access-Control-Allow-Methods";
public static final String ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin";
public static final String ACCESS_CONTROL_EXPOSE_HEADERS = "Access-Control-Expose-Headers";
public static final String ACCESS_CONTROL_MAX_AGE = "Access-Control-Max-Age";
public static final String ACCESS_CONTROL_REQUEST_HEADERS = "Access-Control-Request-Headers";
public static final String ACCESS_CONTROL_REQUEST_METHOD = "Access-Control-Request-Method";
public static final String AGE = "Age";
public static final String ALLOW = "Allow";
public static final String AUTHORIZATION = "Authorization";
public static final String CACHE_CONTROL = "Cache-Control";
public static final String CONNECTION = "Connection";
public static final String CONTENT_ENCODING = "Content-Encoding";
public static final String CONTENT_DISPOSITION = "Content-Disposition";
public static final String CONTENT_LANGUAGE = "Content-Language";
public static final String CONTENT_LENGTH = "Content-Length";
public static final String CONTENT_LOCATION = "Content-Location";
public static final String CONTENT_RANGE = "Content-Range";
public static final String CONTENT_TYPE = "Content-Type";
public static final String COOKIE = "Cookie";
public static final String DATE = "Date";
public static final String ETAG = "ETag";
public static final String EXPECT = "Expect";
public static final String EXPIRES = "Expires";
public static final String FROM = "From";
public static final String HOST = "Host";
public static final String IF_MATCH = "If-Match";
public static final String IF_MODIFIED_SINCE = "If-Modified-Since";
public static final String IF_NONE_MATCH = "If-None-Match";
public static final String IF_RANGE = "If-Range";
public static final String IF_UNMODIFIED_SINCE = "If-Unmodified-Since";
public static final String LAST_MODIFIED = "Last-Modified";
public static final String LINK = "Link";
public static final String LOCATION = "Location";
public static final String MAX_FORWARDS = "Max-Forwards";
public static final String ORIGIN = "Origin";
public static final String PRAGMA = "Pragma";
public static final String PROXY_AUTHENTICATE = "Proxy-Authenticate";
public static final String PROXY_AUTHORIZATION = "Proxy-Authorization";
public static final String RANGE = "Range";
public static final String REFERER = "Referer";
public static final String RETRY_AFTER = "Retry-After";
public static final String SERVER = "Server";
public static final String SET_COOKIE = "Set-Cookie";
public static final String SET_COOKIE2 = "Set-Cookie2";
public static final String TE = "TE";
public static final String TRAILER = "Trailer";
public static final String TRANSFER_ENCODING = "Transfer-Encoding";
public static final String UPGRADE = "Upgrade";
public static final String USER_AGENT = "User-Agent";
public static final String VARY = "Vary";
public static final String VIA = "Via";
public static final String WARNING = "Warning";
public static final String WWW_AUTHENTICATE = "WWW-Authenticate";
```


### 3.HttpMethod

```java
import org.springframework.http.HttpMethod;

GET,
HEAD,
POST,
PUT,
PATCH,
DELETE,
OPTIONS,
TRACE;
```


### 4.HttpStatus

```java
import org.springframework.http.HttpStatus;

CONTINUE(100, "Continue"),
SWITCHING_PROTOCOLS(101, "Switching Protocols"),
PROCESSING(102, "Processing"),
CHECKPOINT(103, "Checkpoint"),
OK(200, "OK"),
CREATED(201, "Created"),
ACCEPTED(202, "Accepted"),
NON_AUTHORITATIVE_INFORMATION(203, "Non-Authoritative Information"),
NO_CONTENT(204, "No Content"),
RESET_CONTENT(205, "Reset Content"),
PARTIAL_CONTENT(206, "Partial Content"),
MULTI_STATUS(207, "Multi-Status"),
ALREADY_REPORTED(208, "Already Reported"),
IM_USED(226, "IM Used"),
MULTIPLE_CHOICES(300, "Multiple Choices"),
MOVED_PERMANENTLY(301, "Moved Permanently"),
FOUND(302, "Found"),
/** @deprecated */
@Deprecated
MOVED_TEMPORARILY(302, "Moved Temporarily"),
SEE_OTHER(303, "See Other"),
NOT_MODIFIED(304, "Not Modified"),
/** @deprecated */
@Deprecated
USE_PROXY(305, "Use Proxy"),
TEMPORARY_REDIRECT(307, "Temporary Redirect"),
PERMANENT_REDIRECT(308, "Permanent Redirect"),
BAD_REQUEST(400, "Bad Request"),
UNAUTHORIZED(401, "Unauthorized"),
PAYMENT_REQUIRED(402, "Payment Required"),
FORBIDDEN(403, "Forbidden"),
NOT_FOUND(404, "Not Found"),
METHOD_NOT_ALLOWED(405, "Method Not Allowed"),
NOT_ACCEPTABLE(406, "Not Acceptable"),
PROXY_AUTHENTICATION_REQUIRED(407, "Proxy Authentication Required"),
REQUEST_TIMEOUT(408, "Request Timeout"),
CONFLICT(409, "Conflict"),
GONE(410, "Gone"),
LENGTH_REQUIRED(411, "Length Required"),
PRECONDITION_FAILED(412, "Precondition Failed"),
PAYLOAD_TOO_LARGE(413, "Payload Too Large"),
/** @deprecated */
@Deprecated
REQUEST_ENTITY_TOO_LARGE(413, "Request Entity Too Large"),
URI_TOO_LONG(414, "URI Too Long"),
/** @deprecated */
@Deprecated
REQUEST_URI_TOO_LONG(414, "Request-URI Too Long"),
UNSUPPORTED_MEDIA_TYPE(415, "Unsupported Media Type"),
REQUESTED_RANGE_NOT_SATISFIABLE(416, "Requested range not satisfiable"),
EXPECTATION_FAILED(417, "Expectation Failed"),
I_AM_A_TEAPOT(418, "I'm a teapot"),
/** @deprecated */
@Deprecated
INSUFFICIENT_SPACE_ON_RESOURCE(419, "Insufficient Space On Resource"),
/** @deprecated */
@Deprecated
METHOD_FAILURE(420, "Method Failure"),
/** @deprecated */
@Deprecated
DESTINATION_LOCKED(421, "Destination Locked"),
UNPROCESSABLE_ENTITY(422, "Unprocessable Entity"),
LOCKED(423, "Locked"),
FAILED_DEPENDENCY(424, "Failed Dependency"),
UPGRADE_REQUIRED(426, "Upgrade Required"),
PRECONDITION_REQUIRED(428, "Precondition Required"),
TOO_MANY_REQUESTS(429, "Too Many Requests"),
REQUEST_HEADER_FIELDS_TOO_LARGE(431, "Request Header Fields Too Large"),
UNAVAILABLE_FOR_LEGAL_REASONS(451, "Unavailable For Legal Reasons"),
INTERNAL_SERVER_ERROR(500, "Internal Server Error"),
NOT_IMPLEMENTED(501, "Not Implemented"),
BAD_GATEWAY(502, "Bad Gateway"),
SERVICE_UNAVAILABLE(503, "Service Unavailable"),
GATEWAY_TIMEOUT(504, "Gateway Timeout"),
HTTP_VERSION_NOT_SUPPORTED(505, "HTTP Version not supported"),
VARIANT_ALSO_NEGOTIATES(506, "Variant Also Negotiates"),
INSUFFICIENT_STORAGE(507, "Insufficient Storage"),
LOOP_DETECTED(508, "Loop Detected"),
BANDWIDTH_LIMIT_EXCEEDED(509, "Bandwidth Limit Exceeded"),
NOT_EXTENDED(510, "Not Extended"),
NETWORK_AUTHENTICATION_REQUIRED(511, "Network Authentication Required");
```


### 5.MediaType

```java
import org.springframework.http.MediaType;

public static final MediaType ALL = valueOf("*/*");
public static final String ALL_VALUE = "*/*";
public static final MediaType APPLICATION_ATOM_XML = valueOf("application/atom+xml");
public static final String APPLICATION_ATOM_XML_VALUE = "application/atom+xml";
public static final MediaType APPLICATION_FORM_URLENCODED = valueOf("application/x-www-form-urlencoded");
public static final String APPLICATION_FORM_URLENCODED_VALUE = "application/x-www-form-urlencoded";
public static final MediaType APPLICATION_JSON = valueOf("application/json");
public static final String APPLICATION_JSON_VALUE = "application/json";
public static final MediaType APPLICATION_JSON_UTF8 = valueOf("application/json;charset=UTF-8");
public static final String APPLICATION_JSON_UTF8_VALUE = "application/json;charset=UTF-8";
public static final MediaType APPLICATION_OCTET_STREAM = valueOf("application/octet-stream");
public static final String APPLICATION_OCTET_STREAM_VALUE = "application/octet-stream";
public static final MediaType APPLICATION_PDF = valueOf("application/pdf");
public static final String APPLICATION_PDF_VALUE = "application/pdf";
public static final MediaType APPLICATION_PROBLEM_JSON = valueOf("application/problem+json");
public static final String APPLICATION_PROBLEM_JSON_VALUE = "application/problem+json";
public static final MediaType APPLICATION_PROBLEM_JSON_UTF8 = valueOf("application/problem+json;charset=UTF-8");
public static final String APPLICATION_PROBLEM_JSON_UTF8_VALUE = "application/problem+json;charset=UTF-8";
public static final MediaType APPLICATION_PROBLEM_XML = valueOf("application/problem+xml");
public static final String APPLICATION_PROBLEM_XML_VALUE = "application/problem+xml";
public static final MediaType APPLICATION_RSS_XML = valueOf("application/rss+xml");
public static final String APPLICATION_RSS_XML_VALUE = "application/rss+xml";
public static final MediaType APPLICATION_STREAM_JSON = valueOf("application/stream+json");
public static final String APPLICATION_STREAM_JSON_VALUE = "application/stream+json";
public static final MediaType APPLICATION_XHTML_XML = valueOf("application/xhtml+xml");
public static final String APPLICATION_XHTML_XML_VALUE = "application/xhtml+xml";
public static final MediaType APPLICATION_XML = valueOf("application/xml");
public static final String APPLICATION_XML_VALUE = "application/xml";
public static final MediaType IMAGE_GIF = valueOf("image/gif");
public static final String IMAGE_GIF_VALUE = "image/gif";
public static final MediaType IMAGE_JPEG = valueOf("image/jpeg");
public static final String IMAGE_JPEG_VALUE = "image/jpeg";
public static final MediaType IMAGE_PNG = valueOf("image/png");
public static final String IMAGE_PNG_VALUE = "image/png";
public static final MediaType MULTIPART_FORM_DATA = valueOf("multipart/form-data");
public static final String MULTIPART_FORM_DATA_VALUE = "multipart/form-data";
public static final MediaType TEXT_EVENT_STREAM = valueOf("text/event-stream");
public static final String TEXT_EVENT_STREAM_VALUE = "text/event-stream";
public static final MediaType TEXT_HTML = valueOf("text/html");
public static final String TEXT_HTML_VALUE = "text/html";
public static final MediaType TEXT_MARKDOWN = valueOf("text/markdown");
public static final String TEXT_MARKDOWN_VALUE = "text/markdown";
public static final MediaType TEXT_PLAIN = valueOf("text/plain");
public static final String TEXT_PLAIN_VALUE = "text/plain";
public static final MediaType TEXT_XML = valueOf("text/xml");
public static final String TEXT_XML_VALUE = "text/xml";
private static final String PARAM_QUALITY_FACTOR = "q";
```





