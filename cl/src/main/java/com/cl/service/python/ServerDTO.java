package com.cl.service.python;

/**
 * Autogenerated by Thrift Compiler (0.9.3)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
import org.apache.thrift.scheme.IScheme;
import org.apache.thrift.scheme.SchemeFactory;
import org.apache.thrift.scheme.StandardScheme;

import org.apache.thrift.scheme.TupleScheme;
import org.apache.thrift.protocol.TTupleProtocol;
import org.apache.thrift.protocol.TProtocolException;
import org.apache.thrift.EncodingUtils;
import org.apache.thrift.TException;
import org.apache.thrift.async.AsyncMethodCallback;
import org.apache.thrift.server.AbstractNonblockingServer.*;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.EnumMap;
import java.util.Set;
import java.util.HashSet;
import java.util.EnumSet;
import java.util.Collections;
import java.util.BitSet;
import java.nio.ByteBuffer;
import java.util.Arrays;
import javax.annotation.Generated;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@SuppressWarnings({"cast", "rawtypes", "serial", "unchecked"})
@Generated(value = "Autogenerated by Thrift Compiler (0.9.3)", date = "2015-10-29")
public class ServerDTO implements org.apache.thrift.TBase<ServerDTO, ServerDTO._Fields>, java.io.Serializable, Cloneable, Comparable<ServerDTO> {
  private static final org.apache.thrift.protocol.TStruct STRUCT_DESC = new org.apache.thrift.protocol.TStruct("ServerDTO");

  private static final org.apache.thrift.protocol.TField AVAILABLE_FIELD_DESC = new org.apache.thrift.protocol.TField("available", org.apache.thrift.protocol.TType.BOOL, (short)1);
  private static final org.apache.thrift.protocol.TField HOSTNAME_FIELD_DESC = new org.apache.thrift.protocol.TField("hostname", org.apache.thrift.protocol.TType.STRING, (short)2);

  private static final Map<Class<? extends IScheme>, SchemeFactory> schemes = new HashMap<Class<? extends IScheme>, SchemeFactory>();
  static {
    schemes.put(StandardScheme.class, new ServerDTOStandardSchemeFactory());
    schemes.put(TupleScheme.class, new ServerDTOTupleSchemeFactory());
  }

  public boolean available; // required
  public String hostname; // required

  /** The set of fields this struct contains, along with convenience methods for finding and manipulating them. */
  public enum _Fields implements org.apache.thrift.TFieldIdEnum {
    AVAILABLE((short)1, "available"),
    HOSTNAME((short)2, "hostname");

    private static final Map<String, _Fields> byName = new HashMap<String, _Fields>();

    static {
      for (_Fields field : EnumSet.allOf(_Fields.class)) {
        byName.put(field.getFieldName(), field);
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, or null if its not found.
     */
    public static _Fields findByThriftId(int fieldId) {
      switch(fieldId) {
        case 1: // AVAILABLE
          return AVAILABLE;
        case 2: // HOSTNAME
          return HOSTNAME;
        default:
          return null;
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, throwing an exception
     * if it is not found.
     */
    public static _Fields findByThriftIdOrThrow(int fieldId) {
      _Fields fields = findByThriftId(fieldId);
      if (fields == null) throw new IllegalArgumentException("Field " + fieldId + " doesn't exist!");
      return fields;
    }

    /**
     * Find the _Fields constant that matches name, or null if its not found.
     */
    public static _Fields findByName(String name) {
      return byName.get(name);
    }

    private final short _thriftId;
    private final String _fieldName;

    _Fields(short thriftId, String fieldName) {
      _thriftId = thriftId;
      _fieldName = fieldName;
    }

    public short getThriftFieldId() {
      return _thriftId;
    }

    public String getFieldName() {
      return _fieldName;
    }
  }

  // isset id assignments
  private static final int __AVAILABLE_ISSET_ID = 0;
  private byte __isset_bitfield = 0;
  public static final Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> metaDataMap;
  static {
    Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> tmpMap = new EnumMap<_Fields, org.apache.thrift.meta_data.FieldMetaData>(_Fields.class);
    tmpMap.put(_Fields.AVAILABLE, new org.apache.thrift.meta_data.FieldMetaData("available", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.BOOL)));
    tmpMap.put(_Fields.HOSTNAME, new org.apache.thrift.meta_data.FieldMetaData("hostname", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    metaDataMap = Collections.unmodifiableMap(tmpMap);
    org.apache.thrift.meta_data.FieldMetaData.addStructMetaDataMap(ServerDTO.class, metaDataMap);
  }

  public ServerDTO() {
  }

  public ServerDTO(
    boolean available,
    String hostname)
  {
    this();
    this.available = available;
    setAvailableIsSet(true);
    this.hostname = hostname;
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public ServerDTO(ServerDTO other) {
    __isset_bitfield = other.__isset_bitfield;
    this.available = other.available;
    if (other.isSetHostname()) {
      this.hostname = other.hostname;
    }
  }

  public ServerDTO deepCopy() {
    return new ServerDTO(this);
  }

  @Override
  public void clear() {
    setAvailableIsSet(false);
    this.available = false;
    this.hostname = null;
  }

  public boolean isAvailable() {
    return this.available;
  }

  public ServerDTO setAvailable(boolean available) {
    this.available = available;
    setAvailableIsSet(true);
    return this;
  }

  public void unsetAvailable() {
    __isset_bitfield = EncodingUtils.clearBit(__isset_bitfield, __AVAILABLE_ISSET_ID);
  }

  /** Returns true if field available is set (has been assigned a value) and false otherwise */
  public boolean isSetAvailable() {
    return EncodingUtils.testBit(__isset_bitfield, __AVAILABLE_ISSET_ID);
  }

  public void setAvailableIsSet(boolean value) {
    __isset_bitfield = EncodingUtils.setBit(__isset_bitfield, __AVAILABLE_ISSET_ID, value);
  }

  public String getHostname() {
    return this.hostname;
  }

  public ServerDTO setHostname(String hostname) {
    this.hostname = hostname;
    return this;
  }

  public void unsetHostname() {
    this.hostname = null;
  }

  /** Returns true if field hostname is set (has been assigned a value) and false otherwise */
  public boolean isSetHostname() {
    return this.hostname != null;
  }

  public void setHostnameIsSet(boolean value) {
    if (!value) {
      this.hostname = null;
    }
  }

  public void setFieldValue(_Fields field, Object value) {
    switch (field) {
    case AVAILABLE:
      if (value == null) {
        unsetAvailable();
      } else {
        setAvailable((Boolean)value);
      }
      break;

    case HOSTNAME:
      if (value == null) {
        unsetHostname();
      } else {
        setHostname((String)value);
      }
      break;

    }
  }

  public Object getFieldValue(_Fields field) {
    switch (field) {
    case AVAILABLE:
      return isAvailable();

    case HOSTNAME:
      return getHostname();

    }
    throw new IllegalStateException();
  }

  /** Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise */
  public boolean isSet(_Fields field) {
    if (field == null) {
      throw new IllegalArgumentException();
    }

    switch (field) {
    case AVAILABLE:
      return isSetAvailable();
    case HOSTNAME:
      return isSetHostname();
    }
    throw new IllegalStateException();
  }

  @Override
  public boolean equals(Object that) {
    if (that == null)
      return false;
    if (that instanceof ServerDTO)
      return this.equals((ServerDTO)that);
    return false;
  }

  public boolean equals(ServerDTO that) {
    if (that == null)
      return false;

    boolean this_present_available = true;
    boolean that_present_available = true;
    if (this_present_available || that_present_available) {
      if (!(this_present_available && that_present_available))
        return false;
      if (this.available != that.available)
        return false;
    }

    boolean this_present_hostname = true && this.isSetHostname();
    boolean that_present_hostname = true && that.isSetHostname();
    if (this_present_hostname || that_present_hostname) {
      if (!(this_present_hostname && that_present_hostname))
        return false;
      if (!this.hostname.equals(that.hostname))
        return false;
    }

    return true;
  }

  @Override
  public int hashCode() {
    List<Object> list = new ArrayList<Object>();

    boolean present_available = true;
    list.add(present_available);
    if (present_available)
      list.add(available);

    boolean present_hostname = true && (isSetHostname());
    list.add(present_hostname);
    if (present_hostname)
      list.add(hostname);

    return list.hashCode();
  }

  @Override
  public int compareTo(ServerDTO other) {
    if (!getClass().equals(other.getClass())) {
      return getClass().getName().compareTo(other.getClass().getName());
    }

    int lastComparison = 0;

    lastComparison = Boolean.valueOf(isSetAvailable()).compareTo(other.isSetAvailable());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetAvailable()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.available, other.available);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetHostname()).compareTo(other.isSetHostname());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetHostname()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.hostname, other.hostname);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    return 0;
  }

  public _Fields fieldForId(int fieldId) {
    return _Fields.findByThriftId(fieldId);
  }

  public void read(org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
    schemes.get(iprot.getScheme()).getScheme().read(iprot, this);
  }

  public void write(org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
    schemes.get(oprot.getScheme()).getScheme().write(oprot, this);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder("ServerDTO(");
    boolean first = true;

    sb.append("available:");
    sb.append(this.available);
    first = false;
    if (!first) sb.append(", ");
    sb.append("hostname:");
    if (this.hostname == null) {
      sb.append("null");
    } else {
      sb.append(this.hostname);
    }
    first = false;
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws org.apache.thrift.TException {
    // check for required fields
    // check for sub-struct validity
  }

  private void writeObject(java.io.ObjectOutputStream out) throws java.io.IOException {
    try {
      write(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(out)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private void readObject(java.io.ObjectInputStream in) throws java.io.IOException, ClassNotFoundException {
    try {
      // it doesn't seem like you should have to do this, but java serialization is wacky, and doesn't call the default constructor.
      __isset_bitfield = 0;
      read(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(in)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private static class ServerDTOStandardSchemeFactory implements SchemeFactory {
    public ServerDTOStandardScheme getScheme() {
      return new ServerDTOStandardScheme();
    }
  }

  private static class ServerDTOStandardScheme extends StandardScheme<ServerDTO> {

    public void read(org.apache.thrift.protocol.TProtocol iprot, ServerDTO struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TField schemeField;
      iprot.readStructBegin();
      while (true)
      {
        schemeField = iprot.readFieldBegin();
        if (schemeField.type == org.apache.thrift.protocol.TType.STOP) { 
          break;
        }
        switch (schemeField.id) {
          case 1: // AVAILABLE
            if (schemeField.type == org.apache.thrift.protocol.TType.BOOL) {
              struct.available = iprot.readBool();
              struct.setAvailableIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 2: // HOSTNAME
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.hostname = iprot.readString();
              struct.setHostnameIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          default:
            org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
        }
        iprot.readFieldEnd();
      }
      iprot.readStructEnd();

      // check for required fields of primitive type, which can't be checked in the validate method
      struct.validate();
    }

    public void write(org.apache.thrift.protocol.TProtocol oprot, ServerDTO struct) throws org.apache.thrift.TException {
      struct.validate();

      oprot.writeStructBegin(STRUCT_DESC);
      oprot.writeFieldBegin(AVAILABLE_FIELD_DESC);
      oprot.writeBool(struct.available);
      oprot.writeFieldEnd();
      if (struct.hostname != null) {
        oprot.writeFieldBegin(HOSTNAME_FIELD_DESC);
        oprot.writeString(struct.hostname);
        oprot.writeFieldEnd();
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

  }

  private static class ServerDTOTupleSchemeFactory implements SchemeFactory {
    public ServerDTOTupleScheme getScheme() {
      return new ServerDTOTupleScheme();
    }
  }

  private static class ServerDTOTupleScheme extends TupleScheme<ServerDTO> {

    @Override
    public void write(org.apache.thrift.protocol.TProtocol prot, ServerDTO struct) throws org.apache.thrift.TException {
      TTupleProtocol oprot = (TTupleProtocol) prot;
      BitSet optionals = new BitSet();
      if (struct.isSetAvailable()) {
        optionals.set(0);
      }
      if (struct.isSetHostname()) {
        optionals.set(1);
      }
      oprot.writeBitSet(optionals, 2);
      if (struct.isSetAvailable()) {
        oprot.writeBool(struct.available);
      }
      if (struct.isSetHostname()) {
        oprot.writeString(struct.hostname);
      }
    }

    @Override
    public void read(org.apache.thrift.protocol.TProtocol prot, ServerDTO struct) throws org.apache.thrift.TException {
      TTupleProtocol iprot = (TTupleProtocol) prot;
      BitSet incoming = iprot.readBitSet(2);
      if (incoming.get(0)) {
        struct.available = iprot.readBool();
        struct.setAvailableIsSet(true);
      }
      if (incoming.get(1)) {
        struct.hostname = iprot.readString();
        struct.setHostnameIsSet(true);
      }
    }
  }

}

